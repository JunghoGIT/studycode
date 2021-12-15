def sum(**kwargs):
    temp = 0
    print(type(kwargs))
    print(kwargs)
    for k,v in kwargs.items():
        print(k,v)
        temp+=v
    print("모든 value의 합은 : {}".format(temp))


sum(a=123,b=100,c=200)

