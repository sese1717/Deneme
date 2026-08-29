class User:

    active_users = 0
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

print(f"Aktif kullanıcı sayısı : {User.active_users}")
u1 = User("Sese","Selim Emir","OCAK",23)
u2 = User("Neco","Necmettin İlker","OCAK",22)
u3 = User("Kemkem","Kemal","YALÇIN",25)
u4 = User("Kemkem","Kemal","YALÇIN",25)
print(f"Aktif kullanıcı sayısı : {User.active_users}")
print(u2.logout())
print(f"Aktif kullanıcı sayısı : {User.active_users}")

