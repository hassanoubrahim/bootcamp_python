import sys

s = ' '.join(sys.argv[1::])
s = s.swapcase()[::-1]
print(s)
