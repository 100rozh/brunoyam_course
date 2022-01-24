x = int(input())
y = int(input())
z = int(input())
match = (x == y) * 1 + (x == z) * 1 + (y == z) * 1
if match == 1:
	print(2)
else:
	print(match)