# file = open("text.txt")

# file.close()
try:
    with open("text.txt") as file:
        for i in file:
            print(i,end="")
except FileNotFoundError as e:
    print("Dosya bulunamadı",e)
finally:
    print("Dosya kapatıldı")

# print(file.read())

# print(file.closed)