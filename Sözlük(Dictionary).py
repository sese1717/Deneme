# 34 => İstanbul
# 35 => İzmir

sehirler = ["İstanbul","İzmir"]
plakalar = [34,35]

print(plakalar[0],sehirler[0]) # 34 İstanbul
print(plakalar[1],sehirler[1]) # 35 İzmir

print(plakalar[sehirler.index("İstanbul")]) # 0 Kaçıncı indexte olduğunu verir. Yani 0. indexte olduğunu söyler.
print(sehirler.index("İzmir")) # 1 Kaçıncı indexte olduğunu verir. Yani 1. indexte olduğunu söyler.

# Key-Value mantığı ile çalışır. Yani plakalar key, şehirler value olarak çalışır.

plakalar = {34: "İstanbul", 35: "İzmir"} # sözlük veri tipinde key-value mantığı ile çalışır. Yani plakalar key, şehirler value olarak çalışır. süslü parantez ile tanımlanır.

print(plakalar[34]) # 34 keyine karşılık gelen value olan İstanbul'u verir.
print(plakalar[35]) # 35 keyine karşılık gelen value olan İzmir'i verir.

plakalar[17] = "Çanakkale" # 17 keyine karşılık gelen value olan Çanakkale'yi ekler.
print(plakalar) # {34: 'İstanbul', 35: 'İzmir', 17: 'Çanakkale'} sözlüğü yazdırır.

print(plakalar[17]) # 17 keyine karşılık gelen value olan Çanakkale'yi verir.

urunler = {100: {"urunAdi" : "Monitör","urunAciklamasi" : "16 in.", "garantiSuresi" : 3, "fiyat": 800}, 101: {"urunAdi" : "Klavye","urunAciklamasi" : "Mekanik", "garantiSuresi" : 2, "fiyat": 500}, 102: {"urunAdi" : "Mouse","urunAciklamasi" : "Kablosuz", "garantiSuresi" : 1, "fiyat": 300}}
print(urunler[100]) # 100 keyine karşılık gelen value olan Monitör'ü verir.

print(urunler[100]["urunAdi"]) # 100 keyine karşılık gelen value olan Monitör'ü verir.
urunler[100]["urunAdi"] = "Monitör 2" # 100 keyine karşılık gelen value olan Monitör'ü Monitör 2 olarak değiştirir.
print(urunler[100]["fiyat"]) # 100 keyine karşılık gelen value olan 800'ü verir.

tutar = urunler[100]["fiyat"] + urunler[101]["fiyat"] + urunler[102]["fiyat"] # 100, 101 ve 102 keyine karşılık gelen value olan fiyatları toplar.
print(tutar) # 1600 toplamını verir.