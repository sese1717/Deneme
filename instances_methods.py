class User :
    # yapıcı metot
    def __init__(self,username,name,surname,birthday) :
        # object attribute, instance attribute
        self.username = username
        self.name = name
        self.surname = surname
        self.birthday = birthday
    # instance methods
    def info (self):
        return f"{self.username} kullanıcı adıyla {self.name.capitalize()} {self.surname} sisteme kaydedildi."

    def calculate_age(self):
        return f"{self.username} kullanıcısının yaşı: {2026-self.birthday}"

u1 = User("Sese","selim Emir","OCAK",2003)
u2 = User("Neco","secmettin İlker","OCAK",2004)

print(u1.info())
print(u2.info())

print(u1.calculate_age())
print(u2.calculate_age())
