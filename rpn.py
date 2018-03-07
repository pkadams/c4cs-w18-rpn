#!/usr/bin/env python 3

import operator
import logging
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
sh = logging.StreamHandler(sys.stdout)
logger.addHandler(sh)

operators = {
	'+': operator.add,
	'-': operator.sub,
	'/': operator.truediv,
	'*': operator.mul,
	
}

def calculate(arg):
	stack = list()
	for token in arg.split():
		try:
			value = int(token)
			stack.append(value)
		except ValueError:
			function = operators[token]
			arg2 = stack.pop()
			arg1 = stack.pop()
			result = function(arg1, arg2)
			stack.append(result)
		logger.debug(stack)
	if len(stack) != 1:
		raise TypeError
	return stack.pop()

def main():
	while True:
		print(calculate(input('rpn calc>')))
		
		

if __name__ == '__main__':
	main()


