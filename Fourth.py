alien_color = 'green'
if alien_color == 'green' :
    print("player earned 5 pts".title())

p = 15
if p < 2:
    print("baby")
elif p > 2 and p < 4 :
    print("toddler")
elif p > 4 and p < 13 :
    print("kid")
elif p > 13 and p < 20 :
    print("teenager")
elif p > 20 and p < 65 :
    print("adult")
elif p > 65 :
    print("elder")

Fruit_list = ['banana', 'apple', 'grapes', 'cherries']
if 'Grapes'.lower() in Fruit_list :
    print(f"you really like grapes".title())

Admin = ['Raf', 'Abdou', 'Admin', 'Hb', 'Ronda']
if Admin : 
    for U in Admin :
        if U.lower() == 'admin' :
            print("Hello admin what do u want to see".title())
        else : 
            print(f"Hello {U.title()}")
else : 
    print("empty list".title())