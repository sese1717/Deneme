class User:

    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"{cls.active_users} tane aktif kullanıcı mevcut."

    @classmethod
    def from_string(cls,data_str):
        username,name,surname,age = data_str.split(",")
        return cls(username,name,surname,age)


    def __init__(self,username,name,surname,age):
        self.username = username
        self.name = name
        self.surname = surname
        self.age = age
        User.active_users += 1

    def username(self):
        return f"{self.username}"

    def logout(self):
        User.active_users -= 1
        return f"{self.username} programdan çıkış yaptı."

print(User.display_active_users())
# u1 = User("Sese","Selim Emir","OCAK",23)
# u2 = User("Neco","Necmettin İlker","OCAK",22)
# u3 = User("Kemkem","Kemal","YALÇIN",25)
# u4 = User("Kemkem","Kemal","YALÇIN",25)

u5 = User.from_string("Eray_sonmez,Eray,SÖNMEZ,24")

print(User.display_active_users())
print(u5.username)
print(u5.name)
print(u5.surname)

