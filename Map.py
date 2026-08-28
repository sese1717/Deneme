sayilar = [1,3,5,8,12]

kareleri = []

# for i in sayilar:
#     kareleri.append(i**2)
# print(kareleri)

def kareAl(sayi):
    return(sayi ** 2)
# sonuc = list(map(kareAl,sayilar))
sonuc = list(map(lambda sayi: sayi ** 2, sayilar))


print(sonuc)

sayi = 1.12412515125

print(f"{sayi:.2f}")