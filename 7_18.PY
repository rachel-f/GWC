number = 79
user guess = input("Guess my lucky number.")

if number == int(user_guess):
	print("You guessed the right number!")
elif number < int(user_guess):
	print("Your guess is too high!")
else:
	print("Your guess is too low!")
	
print("the game is now over")
