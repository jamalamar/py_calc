
secret_word = "giraffe"
guess = ""
tries = 3


while guess != secret_word and tries > 0:
	guess = input("Enter guess: ")
	
	tries -= 1
	
	if tries == 0:
		print("Game Over")

	elif guess == secret_word:
		print("You Win!")