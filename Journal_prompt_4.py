#create a class type Animal
class Animal:
	#-------------------------------
	#initialize instance
	def __init__(self,name,arms,legs,eyes,furry):
		self.name = name
		self.arms = arms
		self.legs = legs
		self.eyes = eyes
		self.furry = furry

	#------------------------------
	def __str__ (self):
		return "Name: " + self.name + "\narms: " + str(self.arms) + "\nlegs: " + str(self.legs) + "\neyes: " + str(self.eyes) + "\nfurry: " + str(self.furry)


a = Animal("Hamster", 2.5, 2.5, 2, True )

print(a)

