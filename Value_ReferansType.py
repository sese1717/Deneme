# Value types => string, number


sayi1 = 10


sayi2 = 20

sayi1 = sayi2

sayi2 = 30

print(sayi1,sayi2)

# Reference types => list, dictionary, set

x = [1,2,3]

y = [4,5,6]

x = y

y[0] = 10

print(x,y) # 2 side değişti çünkü referans tipler bellekte aynı adresi gösterir.