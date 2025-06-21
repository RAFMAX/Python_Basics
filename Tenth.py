"""def sandwhich(*ingredients):
    for ingredient in ingredients:
        print(f"{ingredient.title()} is in the sandwich")
    print("sandwich is prepared")
sandwhich('chicken','beef','tomato')
sandwhich('lettuce','cucumber')"""

def Build_profile(Firstname,Lastname,**Other):
    Other['FirstName'] = Firstname
    Other['LastName'] = Lastname
    return Other

print(Build_profile("Abderraouf", "Benoudina", Age="18", Height="197CM"))
