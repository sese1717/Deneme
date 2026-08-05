iller = ["İstanbul","Ankara","İzmir","Bursa"]

# sonuc = iller

# print(sonuc[0:2])

iller[0] = "Tekirdağ"

sonuc = len(iller) # eleman sayısını sayıp onu verir

print(sonuc)

sonuc = iller + ["Adana","Antalya"] 

del iller[0]
print(sonuc)
print(iller)