#!/usr/bin/env python3

def calculate(arg):
	if arg in {"exit", "quit"}:
		quit()
	stack = []
	tokens = arg.split()
	for tok in tokens:
		if (tok == "+"):
			a = stack.pop()
			b = stack.pop()
			stack.append(a+b)
		else:
			stack.append(float(tok))
	return stack[0]


def main():
	while True:
		calculate(input("rpn calc> "))


if __name__ == "__main__":
	main()