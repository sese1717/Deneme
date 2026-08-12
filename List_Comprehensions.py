# sayilar = []

# for i in range(1,11):
#     sayilar.append(i)
# print(sayilar)

#expression for item in list

# sayilar = [i*2 for i in range(10)]
# print(sayilar)

# liste = [3,8,5,12,40]

# sayilar = [i*2 for i in liste]

# print(sayilar)


sayilar = [1,3,7,12,22,34]

sonuc = []

# for sayi in sayilar:
#     if (sayi % 2 == 0):
#         sonuc.append(sayi)
# print(sonuc)

sayilar = [1,3,7,12,22,34]

sonuc = [sayi for sayi in sayilar if sayi%2==0]
sonu = [sayi if sayi%2==1 else "çift sayı" for sayi in sayilar]
print(sonuc)
print(sonu)