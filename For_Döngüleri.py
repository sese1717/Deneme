
# sayilar = [1,3,6,8,12,16]

# print(sayilar[0])
# print(sayilar[1])
# print(sayilar[2])
# print(sayilar[3])
# print(sayilar[4])
# print(sayilar[5])

# for i in sayilar:
#     print(i)

# for i in sayilar:
#     print("Merhaba")

# isimler = ["Ali","Sinem","Mert","Deniz"]

# for a in isimler:
#     print(a)

# isim = "Selim Emir OCAK"

# for i in isim:
#     print(i)

# _tuple = [(1,2),(3,4),(6,9)]

# for i,b in _tuple:
#     print(i,b)

# iller = {"01":"Adana","02":"Adıyaman","03":"Afyon","04":"Ağrı"}

# for x in iller:
#     print(x)

# for x in iller:
#     print(iller[x])

# for x in iller.values():
#     print(x)

# for key,value in iller.items():
#     print(key,value)

# Uygulama-1

import time

# sensör_verileri = [45,46,47,48,49,50,51,52]

# for i in sensör_verileri:
#     if i > 50:
#         print(f"Sıcaklık kritik değerin üzerinde {i} !!!")
#     else:
#         print(f"Sıcaklık normal düzeyde {i}.")
#     time.sleep(1)


su_sıcaklığı = 0

while (su_sıcaklığı <=50) :
    if (su_sıcaklığı <=45):
        print(f"Su ısıtılıyor {su_sıcaklığı} C*.")
    elif (su_sıcaklığı==48):
        break
    else :
        print(f"Su kritik değeri geçti {su_sıcaklığı} C*.")
    su_sıcaklığı += 1
    time.sleep(0.25)
