class Dog:

	def __init__(self, name, age):	#__init__ is directly called and whats in is directly excuted
		self.name = name
		self.age = age
	
	def sit(self):
		print(f"{self.name} is now sitting.")
	
	def roll_over(self):
		print(f"{self.name} rolled over!")
	
	def get_title(self):
		return(f"{self.name} is upper")
Slougi = Dog('Chiba', 3)			#the name written before the equal is always self Slougi.name == Chiba / Slougi.age == 3 these arguments go to init only
Slougi.sit()						#calls sit with slougi here arguments go to the method only
print(Slougi.get_title())
