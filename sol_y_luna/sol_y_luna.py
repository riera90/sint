import sys

class Tabletop:
	def __init__(self,_n_elem):
		self.table=[]
		self.iteration=0
		self.n_elem=int(_n_elem)
		self.finished_table=[]
		#asignation of default values
		for i in range(0,(self.n_elem*2)+1):
			if i<self.n_elem:
				self.table.append(SHADOW)
			elif i==self.n_elem:
				self.table.append(EMPTY)
			else:
				self.table.append(SUN)

		self.finished_table=self.table[::-1]
		print (self.table)
		print (self.finished_table)

	def print_table(self):
		for i in range(0,(self.n_elem*2)+1):
			sys.stdout.write("____")
		sys.stdout.write("\n")
		sys.stdout.write("| ")
		for i in range(0,(self.n_elem*2)+1):
			sys.stdout.write(self.table[i])
			sys.stdout.write(" | ")
		print ("iteration no: %d"%self.iteration)
		for i in range(0,(self.n_elem*2)+1):
			sys.stdout.write("‾‾‾‾")
		sys.stdout.write("\n")
		return

	def is_finished(self):
		if (list(self.table)==list(self.finished_table)):
			return True
		else:
			return False

	def move_sun(self):
		print("searching...")
		for i in range(1,(self.n_elem*2)+1):
			if self.table[i]==SUN and (self.table[i-1]==EMPTY or (self.table[i-2]==EMPTY and self.table[i-1]==SHADOW)):
				print("bingo!!")
				x=i
				if self.table[i-2]==EMPTY:
					y=i-2
				else:
					y=i-1
				#swap!
				aux=self.table[x]
				self.table[x]=self.table[y]
				self.table[y]=aux
				#end swap :(
				self.iteration+=1
				if self.is_finished():
					return False
				else:
					return True
		print("nope...")
		return False

	def move_shadow(self):
		print("searching...")
		for i in range(0,(self.n_elem*2)):
			if (self.table[i]==SHADOW and ((self.table[i+1]==EMPTY) or (self.table[i+2]==EMPTY and self.table[i+1]==SUN))):
				print("bingo!!")
				x=i
				if self.table[i+2]==EMPTY:
					y=i+2
				else:
					y=i+1
				#swap!
				aux=self.table[x]
				self.table[x]=self.table[y]
				self.table[y]=aux
				#end swap :(
				self.iteration+=1
				if self.is_finished():
					return False
				else:
					return True
		print("nope...")
		return False


	def solve(self):
		if self.n_elem==1:
			self.move_sun()
			self.print_table()
			self.move_shadow()
			self.print_table()
			self.move_sun()
			self.print_table()
			print("\tfinished!")
			return
		else:
			self.print_table()
			solved=False
			if not (self.move_shadow()):
				self.print_table()
				return 0
			else:
				self.print_table()
				while not solved:

					if not (self.move_sun()):
						self.print_table()
						return 0
					else:
						self.print_table()

					if not (self.move_sun()):
						self.print_table()
						return 0
					else:
						self.print_table()

					if not (self.move_shadow()):
						self.print_table()
						return 0
					else:
						self.print_table()

					if not (self.move_shadow()):
						self.print_table()
						return 0
					else:
						self.print_table()

			pass

def main():
	#checks the argument
	if len(sys.argv)<2:
		print("the program needs a comand line argument for the number of elemnts")
		print("sol_y_luna.py <n_elem [1/2]>")
		return

	if int(sys.argv[1])<1 or int(sys.argv[1])>2:
		print("\tinvalid number of elements! enter 1 or 2 elements\n")
		return

	greeting="\tThis program solves the sun and shadow game.\n \tThis is the initial tabletop"
	print(greeting)

	tabletop=Tabletop(int(sys.argv[1]))
	tabletop.solve()
	print ("finished!!!\n")

	return 0

if __name__ == "__main__":
	EMPTY= " "
	SHADOW = "x"
	SUN = "o"
	main()
