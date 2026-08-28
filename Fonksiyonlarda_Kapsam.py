# a = "global değer"

# def fn1():
#     a = "local değer"
#     print(a)

# print(a)
# print(fn1())


# city = "İstanbul"

# def changeCity(new_city):
#     city = new_city
#     print(city)

# changeCity("Bursa")
# print(city)

city = "İstanbul"

def dis_function():
    city = "İzmir"

    def ic_fonksiyon():
        city = "Ankara"
        print("iç fonksiyon"+city)

    ic_fonksiyon()

dis_function()