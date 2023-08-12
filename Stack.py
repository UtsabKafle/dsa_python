from collections import deque


stack = deque()

##creating a stack
for i in "geekbind":
	stack.append(i)

print(stack)


##reversing the string
for i in range(8):
	print(stack.pop(),end="")

