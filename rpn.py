#!/usr/bin/env python3


class CalculatorError(Exception):
	pass


def add(stack):
	if len(stack) < 2:
		raise CalculatorError("stack underflow during addition")
	a = stack.pop()
	b = stack.pop()
	stack.append(a+b)


OPERATORS = {
	"+" : add
}


def calculate(arg):
	if arg.strip() in {"exit", "quit"}:
		quit()
	stack = []
	tokens = arg.split()

	for tok in tokens:
		try:
			stack.append(float(tok))
		except ValueError:
			if tok in OPERATORS:
				OPERATORS[tok](stack)
			else:
				raise CalculatorError("unknown operator \"" + tok + "\"")

	if len(stack) > 1:
		raise CalculatorError("fat stack upon exit")
	if len(stack) == 0:
		raise CalculatorError("empty stack upon exit")
	return stack[0]


def main():
	while True:
		try:
			print(calculate(input("rpn calc> ")))
		except CalculatorError as inst:
			print("Malformed expression: " + inst.args[0])


if __name__ == "__main__":
	main()