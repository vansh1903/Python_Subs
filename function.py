def most_frequent(string):
    sdict = {}
    dict1 = {}
    for i in string:
        c = string.count(i)
        dict1.update({i: c})
    svalue = sorted(dict1.values(), reverse=True)
    for j in svalue:
        for k in dict1.keys():
            if dict1[k] == j:
                sdict[k] = dict1[k]
    print(sdict)


n = input("Enter string:")
most_frequent(n)
