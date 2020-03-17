a = float(input ("видите 1 число: "))
b = float(input("видите 2 число: "))
stroka = input ("видите действие: ")
if stroka == "+":
    print(a+b)
elif stroka == "-":
    print(a-b)
elif stroka == "*":
    print(a*b)
elif stroka == "/":
    print(a/b)
elif stroka == "**":
    print(a*a)
else:
    print("низнаю такого")
