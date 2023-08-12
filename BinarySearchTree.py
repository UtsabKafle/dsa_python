### BinarySearchTree
## A special type of tree with atmost 2 nodes. 

## maintaining a special format in which smaller elements are on left subtree while greater elements are on right subtree


class BST:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

	def add(self,value):
		if value == self.data:
			#if value is already present, just F off; nothing to be done. Duplicates cannot be stored on binary tree
			pass
		if value<self.data:
			# if value is less than the data, go left
			if self.left:
				# if left exists, recursively call the add function.
				self.left.add(value)
			else:
				# if left doesn't exist, meaning it is a leaf node, add a new node of that value
				self.left = BST(value)

		if value>self.data:
			# same as left
			if self.right:
				self.right.add(value)
			else:
				self.right = BST(value)
	def search(self,value):
		if value == self.data:
			# check if value is same as the current node's data
			return "FOUND"
		if value<self.data:
			# if value is less than current node's data
			if self.left:
				# check if left node exists
				# if it does, recursively search in the tree below it until it satisfies the first/above(==) condition or it results as a leaf node
				# and condition goes in the else block and terminates
				return self.left.search(value)
			else:
				return "NOT IN LEFT"
		if value>self.data:
			if self.right:
				return self.right.search(value)
			else:
				return "NOT IN RIGHT"
	def in_order_traversal(self):
		# in InOrderTraversal, the left tree's values are added at left, the root at middle and the right tree's values at right
		elements = []
		## first go through left
		if self.left:
			#go until the leaf node, or self.left = None
			elements += self.left.in_order_traversal()
		# add the node
		elements.append(self.data)
		# add the right
		if self.right:
			elements += self.right.in_order_traversal()
		return elements


	def delete(self,value):
		### deleting value from binary tree
		if  value<self.data:
			# if value is less than current node, go search in the left or smaller subtree
			if self.left:
				self.left =  self.left.delete(value)
		elif value>self.data:
			# if value is more than current node, go search in the right subtree
			if self.right:
				self.right= self.right.delete(value)
		else:
			if self.left is None and self.right is None:
				return None
			elif self.left is None:
				return self.right
			elif self.right is None:
				return self.left
			max_val = self.left.find_max()
			self.data = max_val
			self.left = self.left.delete(max_val)
		return self
	
	def find_max(self):
		## the max value is the right-most leaf node in our binary tree
		if self.right:
			#recursively go down until we reach leaf node
			return self.right.find_max()
		return self.data
	def find_min(self):
		## min value is the left-most leaf node
		if self.left:
		# recursively go down until we reach leaf node
			return self.left.find_min()
		return self.data

def main():
	import random
	#root = BST(43)
	data = [3,4,2,5,2,66,23,2,32,43,-3,55,23,54,23,5,2,55,23,5,2,66,99,34,23,11,44,2,0,64,23]
	## randomly select the root node
	root_node = random.choice(data)
	print(f"root node is {root_node}")
	root = BST(root_node)
	for i in data:
		root.add(i)
	print("before deleting")
	print(root.in_order_traversal())
	root.delete(34)
	print("after deleting 34")
	print(root.in_order_traversal())
if __name__ == "__main__":
	main()
