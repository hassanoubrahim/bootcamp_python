

def text_analyser(text = None):
	if text is None:
		print("What is the text to analyse?")
	else:
		counter = 0
		upper = 0
		lower = 0
		pun = 0
		space = 0
		for i in text:
			if i.isupper():
				upper += 1
			elif i.islower():
				lower += 1
			elif i.isspace():
				space += 1
			else:
				pun += 1
			counter += 1
		print("The text contains", counter, "characters:")
		print("-", upper, "upper letters")
		print("-", lower, "lower letters")
		print("-", pun, "punctuation marks")
		print("-", space, "space")