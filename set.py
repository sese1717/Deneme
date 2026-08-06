# list içerisindeki öğeleri değiştirebiliriz.
# tuple içerisindeki öğeleri değiştiremeyiz.
# dictionary içerisindeki öğeleri değiştirebiliriz. Bir dictionary içerisindeki öğeler key-value şeklinde tutulur. Keyler benzersizdir ve değiştirilemez. Value ise değiştirilebilir.
# sets indeki öğeler benzersizdir ve değiştirilemez. Sets içerisindeki öğeler sırasızdır ve indekslenemez. Sets içerisindeki öğeler değiştirilebilir. Sets içerisindeki öğeler küme mantığı ile çalışır. Sets içerisindeki öğeler matematiksel küme işlemleri ile birleştirilebilir, kesiştirilebilir, farkı alınabilir.

# sets çok verimli bir veri yapısıdır. Sets içerisindeki öğeler benzersizdir ve değiştirilemez. Sets içerisindeki öğeler sırasızdır ve indekslenemez. Sets içerisindeki öğeler değiştirilebilir. Sets içerisindeki öğeler küme mantığı ile çalışır. Sets içerisindeki öğeler matematiksel küme işlemleri ile birleştirilebilir, kesiştirilebilir, farkı alınabilir.

markalar = {"Audi","Mercedes","Bmw","Honda"}

# sonuc = markalar[0] # Sets içerisindeki öğelere indeksleme ile erişemeyiz. Bu nedenle bu satır hata verecektir.

# sorgulama işlemi yapabiliriz.

sonuc = "Bmw" in markalar 

print(sonuc)

# Yeni bir öğe ekleyebiliriz.

markalar.add("Opel")

print(markalar) # Rastgale bir sırada eklenir.

# Birden fazla öğe ekleyebiliriz.

markalar.update(["Toyota","Scoda"])

print(markalar) # Rastgale bir sırada eklenir.

print(len(markalar)) # Sets içerisindeki öğelerin sayısını öğrenebiliriz.

markalar.remove("Opel") # remove() metodu ile öğe silebiliriz. Eğer silmek istediğimiz öğe yoksa hata verir.

print(markalar)

markalar.pop() # pop() metodu ile rastgele bir öğe silebiliriz.

print(markalar)

markalar.clear() # clear() metodu ile tüm öğeleri silebiliriz.

print(markalar)

# Birleşim işlemi yapabiliriz.

markalar1 = {"Audi","Mercedes","Bmw","Honda"}
markalar2 = {"Toyota","Scoda","Bmw","Honda"}

print(markalar1.union(markalar2)) # union() metodu ile birleşim işlemi yapabiliriz.


