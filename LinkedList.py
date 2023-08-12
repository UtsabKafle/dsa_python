class Node:
	def __init__(self,data,next):
		self.data = data
		self.next = next
class LinkedList:
	def __init__(self):
		## we need a head to act as a container for the nodes
		self.head = None
	def insert_b(self,element):
		node = Node(element,self.head)
		self.head = node
		
	def print(self):
		itr = self.head
		llstr = ''
		while itr:
			llstr += str(itr.data)+'-->' if itr.next else str(itr.data)
			itr = itr.next
		print(llstr)
	def insert_beginning(self,element):
		itr = self.head
		#print(f"{()} => {itr.data}")
		while itr:
			print(f"======> {itr.next.data if itr.next else 'crap'}")
			itr = itr.next
			elem = 0
		print(itr)
		node = Node(element,itr)
		itr = node
	
	def insert_end(self,element):
		if self.head is None:
			self.head = Node(element,None)
			return
		itr = self.head
		while itr.next:
			itr = itr.next
		itr.next = Node(element,None)


def main():
	import sys
	ll = LinkedList()
	#print(sys.argv)
	for i in range(1,len(sys.argv)):
		ll.insert_b(sys.argv[i])
	
	ll.insert_end(32)
	#ll.insert(33)
	#ll.insert(3444)
	#ll.insert(323)
	ll.print()


main()

