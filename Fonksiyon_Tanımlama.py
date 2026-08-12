# def karsilama():
#     for i in range(10):
#         print("Merhaba")

# karsilama()

# a = 5
# b = 10

# def carpma():
#     print(a*b)

# carpma()

# Return

# def adin_ne():
#     ad = input("Adınızı giriniz: ")
#     return ad

# # adin_ne()

# print("Sisteme hoş geldniniz",adin_ne())

# def topla():
#     return( 20 + 30 )

# sonuc = topla()*2

# print(sonuc)

saat = 20

def selamla():
    if saat < 12 :
        return ("Günaydın")
    elif saat >= 12 and saat < 18 :
        return "İyi Günler"
    else:
        return "iyi akşamlar"

print(selamla())
