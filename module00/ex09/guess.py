
import random

n = random.randint(0, 99)

print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!\n")

x = ''
counter = 0
while x != n:
	try:
		x = int(input())
		if(x > n):
			print("Too high!")
		elif(n > x):
			print("Too low!")
		counter += 1
	except ValueError:
		if x == 'exit':
			counter = -1
			break
		else:
			print("Thats not a number.")


if counter == 1:
	print("congratulation, you got it on the first try!")
elif counter > 1:
	print("you won with in ",counter,"attemps")
else:
	print("bye")
