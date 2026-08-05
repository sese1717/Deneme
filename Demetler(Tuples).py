# Demet veri setlerinde içerideki bilgiler değiştirilemez. Yani demetler değiştirilemez veri tipidir. Ama demetlerin içindeki listeler değiştirilebilir.

list1 = [1,3,5,13]

thistuple = (1,2,"altı",False,2) #Parantez ile tanımlanır.Parantez olmasa da olur ama parantez kullanmak daha iyi olur.

print(thistuple) #Demeti yazdırır.
print(type(thistuple)) #Demetin veri tipini yazdırır.

print(type(list1)) #Listelerin veri tipini yazdırır.

print(list1[0]) #Listelerin içindeki verilere ulaşmak için köşeli parantez kullanılır.

print(thistuple[2]) #Demetlerin içindeki verilere ulaşmak için köşeli parantez kullanılır.

print(len(list1)) #Listelerin uzunluğunu yazdırır.
print(len(thistuple)) #Demetlerin uzunluğunu yazdırır.

list1[0] = 5 #Listelerin içindeki veriler değiştirilebilir.

print(list1) #Listelerin içindeki veriler değiştirildikten sonra yazdırılır.

# thistuple[0] = 5 #Demetlerin içindeki veriler değiştirilemez. Bu yüzden hata verir.

list1.append(7) #Listelerin içine yeni veri eklenebilir.

thistuple2 = (1,2,3,4,5,6,7,8,9,10) #Demetlerin içine yeni veri eklenemez.

list1.count(3) #Listelerin içinde kaç tane 3 olduğunu sayar.

print(list1.count(3)) #Listelerin içinde kaç tane 3 olduğunu yazdırır.

thistuple.count(3) #Demetlerin içinde kaç tane 3 olduğunu sayar.

print(thistuple.count(3)) #Demetlerin içinde kaç tane 3 olduğunu yazdırır.

thistuple + thistuple2 #Demetlerin içindeki veriler birleştirilebilir.

print(thistuple + thistuple2) #Demetlerin içindeki veriler birleştirildikten sonra yazdırılır.

list2 = tuple([1,2,3,4,5]) #Listeler demetlere dönüştürülebilir.
print(list2) #Listeler demetlere dönüştürüldükten sonra yazdırılır.



