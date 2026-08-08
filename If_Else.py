# sayi = -5

# if (sayi > 0):
#     print("Sayi pozitiftir.")
# elif (sayi < 0): #Else de kullanılabilir. Else if yerine elif kullanılır.
#     print("Sayi negatiftir.")

# if (sayi > 0):
#     print("Sayi pozitiftir.")
# else:
#     print("Sayi negatiftir.")

# giris = True

# if (giris ==True):#Gırısın içinde True olduğu için if zaten çalıştırıcaktı.Bu yüzden ==True yazmamıza gerek yoktu.
#     print("Giriş başarılı.")
# else:
#     print("Giriş başarısız.")

username= "Selim Emir OCAK"
password= "123456"

# if (username == "Selim Emir OCAK" and password == "12345"):
#     print("Giris başarılı.")
# else:
#     print("Giris başarısız.")

if(username == "Selim Emir OCAK"):
    if (password == "12345"):
        print("Giris başarılı.")
    else:
        print("Parola hatalı.")
else:
    print("Kullanıcı adı hatalı.")
