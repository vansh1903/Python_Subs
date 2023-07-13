import requests
from bs4 import BeautifulSoup
import sqlite3
import pandas


def connect():
    conn = sqlite3.connect("country.db")

    conn.execute("CREATE TABLE IF NOT EXISTS COUNTRY_INFO (NAME TEXT, CAPITAL TEXT, POPULATION INT, AREA FLOAT)")

    print("Table created successfully")
    conn.close()


def insert_into_table(values):
    conn = sqlite3.connect("country.db")

    conn.execute("INSERT INTO COUNTRY_INFO (NAME, CAPITAL, POPULATION, AREA) VALUES (?, ?, ?, ?)", values)

    conn.commit()
    conn.close()


def display_info():
    conn = sqlite3.connect("country.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM COUNTRY_INFO")

    table_data = cur.fetchall()
    for record in table_data:
        print(record)

    conn.close()


if __name__ == "__main__":
    url = "https://scrapethissite.com/pages/simple/"

    connect()
    req = requests.get(url)

    scraped_info_list = []

    content = req.content

    soup = BeautifulSoup(content, "html.parser")

    all_countries = soup.find_all("div", {"class": "col-md-4 country"})

    for country in all_countries:
        country_dict = {"country_name": country.find("h3", {"class": "country-name"}).text.strip(),
                        "country_capital": country.find("span", {"class": "country-capital"}).text,
                        "country_pop": country.find("span", {"class": "country-population"}).text,
                        "country_area": country.find("span", {"class": "country-area"}).text}
        print(country_dict.values())
        insert_into_table(tuple(country_dict.values()))
        display_info()
        scraped_info_list.append(country_dict)

    dataframe = pandas.DataFrame(scraped_info_list)
    dataframe.to_csv("country.csv")
