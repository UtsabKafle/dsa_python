class HashTable:
	def __init__(self):
		## allocating and empty list with 100 elements
		self.MAX = 100
		self.arr = [[] for i in range(self.MAX)]
	def get_hash(self,value):
		val = 0
		for char in value:
			val += ord(char)
		val = val % self.MAX
		return val
	def add(self,key,value):
		index = self.get_hash(key)
		for i in range(len(self.arr[index])):
			if self.arr[index][i][0] == key:
				self.arr[index][i] = (key,value)
				return
		self.arr[index].append((key,value))
	def print(self,key):
		index = self.get_hash(key)
		for i in self.arr[index]:
			if i[0] == key:
				return i[1]
		


#  [(key,val),(key2,val2)]
# [(key,val)]
#
#
#
def main():
	a = HashTable()
	a.add('MJ',69)
	a.add('IN',33)
	#print(a.arr)
	a.add('kafle',21)
	print(a.print('MJ'))
	print(a.print('IN'))
	print(a.arr)
if __name__ == "__main__":
	main()
