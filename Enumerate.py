diller = ["Python","Javascript","Flutter"]

index = 0
for i in diller:
    print(f"{index+1}-{diller[index]}")
    index += 1

#enumerata metodu

obje = enumerate(diller)

print(type(obje))
print(list(obje))

for i in enumerate(diller):
    print(i)

for index,value in enumerate(diller,1):
    print(f"{index}-{value}")