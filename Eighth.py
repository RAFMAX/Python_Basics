Top = input("Pizza topping : ")
while Top != 'quit' :
    print(f"we will add {Top} to you pizza".title())
    Top = input("Pizza topping : ")


favlang = {}
Lp = True
while Lp:
    Name = input("Name is : ")
    if Name.lower() == 'quit':
        break
    Lang = input("Fav lang is : ")
    favlang[Name] = Lang
for K, V in favlang.items():
    print(f"{K} loves {V}")

