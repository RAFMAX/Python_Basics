Person2 = {
	'Name': 'D',
	'Age': 19,
    'D': 'D',
	}
print(Person2.get('Name'))
print(Person2['Name'])
V = Person2.get('Height','no height info')
print(Person2.items())
T = [(1,2), (4,5), (6,7)]
for t,v in T:
    print(f"{t}: {v}")


print(set(Person2.values()))