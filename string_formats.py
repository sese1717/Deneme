name = "Selim Emir"
surname = "OCAK"
age = "23"

print("My name is {} {} ".format(name,surname))
print("My name is {1} {0} ".format(name,surname))
print("My name is {s} {n} ".format(n=name,s=surname))
print("My name is {} {}. I'm {} years old. ".format(name,surname,age))
print("My name is {0} {1}. I'm {2} years old. {2} ".format(name,surname,age))

number = 5/3
print("The result is {}.".format(number))
print("The result is {n:1.2}.".format(n=number))

print(f"My name is {name} {surname} and. I am {number:1.2} years old.")
