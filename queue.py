from collections import deque

## Queue is First In First Out data structure.
class Queue_:
	def __init__(self):
		self.queue = deque()
		## creating an deque
	def add(self,value):
		self.queue.appendleft(value)
		##appenleft function adds the value to the 0th index
		## and will move other elements by 1 index
	def _deque(self):
		print(self.queue.pop())



def main():
	q = Queue_()
	q.add(3)
	q.add(4)
	print(q.queue)
	q.add(2)
	q._deque()
	q._deque()
	q._deque()



if __name__ == "__main__":
	main()
