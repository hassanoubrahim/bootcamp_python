import sys



if len(sys.argv) != 3:
	print("InputError: too manyarguments")
	print("Usage : python operations.py <number1> <number2>")
	print("Example:\n\tpython operations.py 10 3")
elif not sys.argv[1].isdigit() or not sys.argv[2].isdigit():
	print("InputError Only numbers")
	print("Usage : python operations.py <number1> <number2>")
	print("Example:\n\tpython operations.py 10 3")
	
else:
	n, m = int(sys.argv[1]), int(sys.argv[2])
	print("Sum:", m+m)
	print("Difference:", n-m)
	print("Product:", n*m)
	if m == 0:
		print("ERROR (div by zero")
		print("modulo by zero")
	else:
		print("Quotient:", m/m) 
		print("Remainder:", n%m)