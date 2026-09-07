def sayac(max):
    sayi = 1

    while sayi <= max:
        yield sayi
        sayi += 1
    

iterator = sayac(20)



# print(next(generator))

for i in iterator:
    print(i)

