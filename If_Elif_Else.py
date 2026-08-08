a = 20
b = 15

if (a > b):
    print("a b'den büyüktür.")
elif (a == b):
    print("a b'ye eşittir.")
else:
    print("a b'den büyük değildir.")

karne_notu = 40

if (karne_notu < 50):
    print("Sınıf tekrarı")
elif (50 <= karne_notu <= 70):
    print("Başarılı herhangi bir başarı belgesi yok.")
elif (70 < karne_notu <= 85):
    print("Taşekkür belgesi")
else:
    print("Taktir belgesi")

# If'ın içinde If kullanırken unutulmamaı gereken şey bir tanesinin başarılı olması diğerini tetikliyo.
 