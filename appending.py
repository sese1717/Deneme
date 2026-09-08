# "r" : (read) okuma modu
# "w" : (write) yazma modu
# "a" : (append) ekleme modu
# "r+" : (read and write) okuma ve yazma modu

with open("text.txt","r+",encoding="utf-8") as file:
   
    file.write("Yeni satır")
    