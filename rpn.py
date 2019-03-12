#!/usr/bin/env python3


class CalculatorError(Exception):
	pass


def add(stack):
	if len(stack) < 2:
		raise CalculatorError("stack underflow during addition")
	b = stack.pop()
	a = stack.pop()
	stack.append(a + b)

def subtract(stack):
	if len(stack) < 2:
		raise CalculatorError("stack underflow during subtraction")
	b = stack.pop()
	a = stack.pop()
	stack.append(a - b)


def multiply(stack):
	if len(stack) < 2:
		raise CalculatorError("stack underflow during multiplication")
	b = stack.pop()
	a = stack.pop()
	stack.append(a * b)


def divide(stack):
	if len(stack) < 2:
		raise CalculatorError("stack underflow during division")
	b = stack.pop()
	a = stack.pop()
	try:
		stack.append(a / b)
	except:
		raise CalculatorError("division by zero")


def power(stack):
	if len(stack) < 2:
		raise CalculatorError("stack underflow during exponentiation")
	b = stack.pop()
	a = stack.pop()
	stack.append(a ** b)


OPERATORS = {
	"+" : add,
	"-" : subtract,
	"*" : multiply,
	"/" : divide,
	"^" : power
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
			expression = input("rpn calc> ")
			if expression.strip() != "":
				print(calculate(expression))
		except CalculatorError as inst:
			print("Malformed expression: " + inst.args[0])


if __name__ == "__main__":
	main()