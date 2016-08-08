import random


protein = ["chicken", "beef", "fish", "beans"]
veggie = ["asparagus", "corn", "green beans", "roasted peppers"]
carb = ["mashed potaoes", "rice", "polenta", "pasta"]
menu = []
random_number = random.randint(0, 3)


#print(protein[random.randint(0,4)])

for i in range (1):
	menu.append(protein[random_number])
	menu.append(veggie[random_number])
	menu.append(carb[random_number])
print(menu)


