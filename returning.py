# def usalma(number):
#     def inner(power):
#         return number ** power
#     return inner

# print(usalma(2)(3))

def islem(islem_adi):
    def toplam(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam
    def carpma(*args):
        carpim = 1
        for i in args:
            carpim *= i
        return carpim
    if islem_adi == "toplama":
        return toplam
    else:
        return carpma

toplama = islem("carpma")

print(toplama(2,4,6,8,10))