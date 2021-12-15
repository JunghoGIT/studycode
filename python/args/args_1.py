def sum(*args):
    print(type(args))
    temp = 0
    for x in args:
        temp+=x
    return temp

temp = (3,4,5)
a = sum(*temp)
print(a)
