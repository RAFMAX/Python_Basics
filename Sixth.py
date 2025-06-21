Rivers = {
    'Nile' : 'Egypt',
    'Furat' : 'Iraq',
    'Dajla' : 'Iraq',
}
for R,C in Rivers.items():
    print(f"{R.title()} is in {C.title()}.")
for R in Rivers.keys():
    print(R)
for C in Rivers.values():
    print(f"{C}")

Dog = {
    'Name': 'Dog',
    'Kind': 'Pitbull',
    'Owner' : 'Md',
}

Cat = {
    'Name': 'Cat',
    'Kind': 'Siamo',
    'Owner' : 'Ld',
}

Bird = {
    'Name': 'Bird',
    'Kind': 'Canari',
    'Owner': 'Ad',
}

Pets = [Dog, Cat, Bird]
for Animal in Pets:
    print(f"The animal is a {Animal['Name']}")
    for K, V in Animal.items():
        if K != 'Name':
            print(f"\tThe {K} is {V}")
