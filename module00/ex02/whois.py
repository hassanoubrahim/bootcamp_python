import sys

if len(sys.argv) > 2 or not sys.argv[1].isdigit():
	print("ERROR")
elif sys.argv[1].isdigit():
	n = int(sys.argv[1])
	if n == 0:
		print("I'm Zero.")
	elif n % 2 == 1:
		print("I'm Odd.")
	elif n % 2 == 0:
		print("I'm Even.")
	else:
		print("ERROR.")
