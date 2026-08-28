class Product :
    def __init__(self, name , price ):
        self.name = name
        self.price = price
        print("Product nesnesi oluşturuldu.")

p1 = Product("Mercedes A","600000")
p2 = Product("BMW 330","500000")
p3 = Product("Opel Astra","300000")

print(p1.name,p1.price)
print(p2.name,p2.price)
print(p3.name,p3.price)
    