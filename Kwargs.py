# def userInfo(*args):
#     print(type(args))

# userInfo()

# def userInfo(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}: {value}")
#         print("\n")
# userInfo(username = "Selim", password="123456", email ="Levent")

def siralama(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(*args)
    print(*kwargs)

siralama(1,2,3,4,5,6,key1 ="value1",key2 = "value2")

