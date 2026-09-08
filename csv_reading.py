import csv

# with open("films.csv") as file:
#     print(file.read())

with open("films.csv") as file:
    csv_reader = csv.reader(file)
    for f in csv_reader:
        print(f"Film adı: {f[0]} - Film Türü: {f[1]} - Film Yılı: {f[2]}")
  