arabaAuidi = {
    "marka" : "Auidi",
    "model" : "A5",
    "yil" : 2019
}

# # Değerlere erişmek için get() metodunu kullanabiliriz.

# sonuc = arabaAuidi["marka"] # Değerleri köşeli parantez ile çağırabiliriz.

# print(sonuc)

# sonuc = arabaAuidi.get("model") # Değerleri get() metodu ile çağırabiliriz.

# print(sonuc)

# #sorgulama in metodu ile de yapılabilir.

# sonuc = "marka" in  arabaAuidi # Sorgulama işlemi yapabiliriz.

# print(sonuc)

# sonuc = len(arabaAuidi) # Uzunluk sorgulaması yapabiliriz.
# print(sonuc)

# # Ekleme işlemi yapabiliriz.
# arabaAuidi["renk"] = "beyaz"
# print(arabaAuidi)

# #silme işlemi yapabiliriz.
# arabaAuidi.pop("yil") # pop() metodu ile silme işlemi yapabiliriz.
# print(arabaAuidi)

# arabaAuidi.popitem() # popitem() metodu ile son eklenen öğeyi silebiliriz.
# print(arabaAuidi)

# del arabaAuidi["model"] # del metodu ile silme işlemi yapabiliriz.
# print(arabaAuidi)

# arabaAuidi.clear() # clear() metodu ile tüm öğeleri silebiliriz.
# print(arabaAuidi)

#Objeyi kopyalamak için copy() metodunu kullanabiliriz.
araba = arabaAuidi.copy()

print(araba)

araba["marka"] = "BMW" # Kopyalanan objeyi değiştirebiliriz.

print(araba)

# Değer güncellemek için update() metodunu kullanabiliriz.
araba.update({"model" : "X5"}) # update() metodu ile değer güncelleyebiliriz.
print(araba)