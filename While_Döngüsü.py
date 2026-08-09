# while True:
#     print("Merhaba")

# i = 0
# while i <= 10:
#     print(i)
#     i += 1

i = 1

# while i <= 100:
#     if (i%2 == 0):
#         print(f"Çift: {i}")
#     else:
#         print(f"Tek:  {i}")
#     i +=1


email = "" #Bu halde çalıştırdığımızda False değerini elde ederiz.Eğer içinde en ufak bir şey olsaydı True değerini elde ederdik.

print(bool(email))

while not email:
    email = input("Email adresinizi giriniz: ")

print("Girdiğiniz email adresi: ",email)

