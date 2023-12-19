def main():
	x = int(input("what's x? "))
	# y = float(input("what's y? "))
	# z = x / y
	# print(f"{z:.2f}")
	print("x squared is", square(x))

def square(n):
	return pow(n, 2)

main()
