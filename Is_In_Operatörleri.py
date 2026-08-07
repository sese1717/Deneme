# Identy operatör : is

x = y = [1,2,3,4]

z = [1,2,3,4]

# is operatörü, iki değişkenin aynı nesneyi işaret edip etmediğini kontrol eder. Yani, iki değişkenin bellekte aynı referansa sahip olup olmadığını kontrol eder.

print(f"x is y : {x is y}") # True, çünkü x ve y aynı listeyi işaret ediyor.

print(f"x is z : {x is z}") # False, çünkü x ve z farklı listeleri işaret ediyor.

print(f"x == y : {x == y}") # True, çünkü x ve y aynı listeyi işaret ediyor.

print(x == z) # Burda eşitler

# Membership operatörü : in

a = ["Python","Javascript"]

print(f"Python a listesinde var mı? : {'Python2' in a}")

email = "deneme@gmail.com"

print(f"@ işareti emailde var mi? : {'@' in email}")