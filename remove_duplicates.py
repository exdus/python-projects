def remove_duplicates(string):
    string = string.lower()
    k = set(string)
    x = list(string)
    value = len(x) - len(k)
    z =list(k)
    #z.sort()
    result = "".join(z),value
    return(tuple(result))

print(remove_duplicates("happy"))
