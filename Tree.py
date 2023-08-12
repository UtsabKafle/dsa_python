class Tree:
	def __init__(self,data):
		self.data = data
		self.children = []
		self.parent = None
	def add_child(self,data):
		data.parent = self
		self.children.append(data)

	def get_level(self):
		level = 0
		p = self.parent
		while p:
			level += 1
			p = p.parent
		return int(level)

	def print_tree(self):
		pref = " " * self.get_level()*4
		print(f"{pref}|-- {self.data}")
		p = self.children
		if p:
			for i in p:
				i.print_tree()
		

def main():
	root = Tree("Videos")
	
	long = Tree("long videos")
	long.add_child(Tree("MR Beast"))
	long.add_child(Tree("JOE Rogan"))
	long.add_child(Tree("Sweatbh gangwar"))



	short = Tree("short videos")
	short.add_child(Tree("Robert Greene"))
	short.add_child(Tree("Funny"))



	root.add_child(long)
	root.add_child(short)
	#root.get_level()
	root.print_tree()


if __name__ == "__main__":
	main()
