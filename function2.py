# encapsulation
# def dis_fonksiyon(sayi1):
#     print("Dış fonksiyon çalışıyor")
#     def ic_fonksiyon(sayi1):
#         print("İç fonksiyon çalışıyor")
#         return sayi1 ** 2
#     sayi2 = ic_fonksiyon(sayi1)
#     print(sayi1,sayi2)

# dis_fonksiyon(5)

def factorial(sayi):
    def ic_faktorial(sayi):
        if sayi <= 1:
            return 1
        return sayi * ic_faktorial(sayi - 1)
    return ic_faktorial(sayi)

print(factorial(5))
