phrase = "The right format"

n = len(phrase)

t = 41 - n
s = ""
while(t > 0):
	s += "-"
	t -= 1
s += phrase

s = ''.join(s)
print(s)