# sayi = int(input("Sayı giriniz: "))

# if (sayi > 0):
#     if (sayi % 2 == 1):
#         print("Girilen sayi pozitif tek sayıdır.")
#     else:
#         print("Girilen sayi pozitif çift sayıdır.")
# elif (sayi == 0):
#     print("Girilen sayi 0'dır")
# else:
#     if (sayi % 2 == 1):
#         print("Girilen sayi negatif tek sayıdır.")
#     else:
#         print("Girilen sayi negatif çift sayıdır.")



# Uygulama 2

# x = int(input("x : "))
# y = int(input("y : "))
# z = int(input("z : "))

# if ( x > y) and (x > z):
#     print("x en büyüktür.")
#     if (y > z):
#         print("x > y > z")
#     else:
#         print("x > z > y")
# elif ( y > x) and (y > z):
#     print("y en büyüktür.")
#     if (x > z):
#         print("y > x > z")
#     else:
#         print("y > z > x")
# elif ( z > y) and (z > x):
#     print("z en büyüktür.")
#     if (y > x):
#         print("z > y > x")
#     else:
#         print("z > x > y")


# Uygulama 3

isim = input("İsminizi giriniz: ")
yas = int(input("Yaş: "))
eğitim = input("Eğitim durumu: ")

if yas >= 18:
    if eğitim == "Lise" or eğitim == "Üniversite":
        print("Ehliyet alabilirsiniz")
    else:
        print(f"{isim} ehliyet alamazsınız")
else:
    print(f"{isim} yaşını tutmuyor.")
