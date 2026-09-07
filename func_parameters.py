def toplama(a,b):
    return a+b

def cıkarma(a,b):
    return a-b

def carpma(a,b):
    return a*b

def bolme(a,b):
    return a/b

def islem(f1,f2,f3,f4,islem_adi):
    if islem_adi =="toplama":
        print(f1(2,4))
    elif islem_adi =="cıkarma":
        print(f2(10,4))
    elif islem_adi =="carpma":
        print(f3(3,7))
    elif islem_adi =="bolme":
        print(f4(20,4))
    else:
        print("Geçersiz işlem")

islem("toplama")