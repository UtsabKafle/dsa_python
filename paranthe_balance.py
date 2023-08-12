from collections import deque


def is_blanaced(string):
	stack = deque()
	for i in string:
		stack.append(i)
	while len(stack):
		if  stack.pop == stack.popleft():
			pass
		else:
			
