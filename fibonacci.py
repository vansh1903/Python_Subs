def rec(n):
    if n <= 1:
        return (n)
    else:
    return (rec(n-1) + rec(n-2))
a = int(input("Enter limit:"))
for i in a:
    print(rec(i))
