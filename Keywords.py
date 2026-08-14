# def fullname(ad,soyad):
#     return f"Sisteme hoş geldiniz, {ad} {soyad}."

# # sonuc = fullname("Selim Emir","OCAK")
# sonuc = fullname(soyad="OCAK",ad="Selim Emir")
# print(sonuc)

#Args 

numbers = [5,15,20,25]


# def topla (a,b):
#     return(a+b)

# def topla(sayilar):
#     sonuc = 0
#     for i in sayilar:
#         sonuc += i
#     return(f"Sayilarin toplamı: {sonuc}")

# print(topla(numbers))

def topla(*args):
    sonuc = 0
    for i in args:
        sonuc += i
    return(sonuc)
print(topla(5,10,15))





