import sys

class Tabletop:
	def __init__(self,_n_elem):
		self._table=[]
		self._iteration=0
		self._n_elem=int(_n_elem)
		self._finished_table=[]
		#asignation of default values
		for i in range(0,(self._n_elem*2)+1):
			if i<self._n_elem:
				self._table.append(SHADOW)
			elif i==self._n_elem:
				self._table.append(EMPTY)
			else:
				self._table.append(SUN)

		self._finished_table=self._table[::-1]
		print (self._table)
		print (self._finished_table)

	def print_table(self):
		for i in range(0,(self._n_elem*2)+1):
			sys.stdout.write("____")
		sys.stdout.write("\n")
		sys.stdout.write("| ")
		for i in range(0,(self._n_elem*2)+1):
			sys.stdout.write(self._table[i])
			sys.stdout.write(" | ")
		print ("iteration no: %d"%self._iteration)
		for i in range(0,(self._n_elem*2)+1):
			sys.stdout.write("‾‾‾‾")
		sys.stdout.write("\n")
		return

	def __is_finished(self):
		if (list(self._table)==list(self._finished_table)):
			return True
		else:
			return False

	def __move_sun(self):
		print("searching...")
		for i in range(1,(self._n_elem*2)+1):
			if self._table[i]==SUN and (self._table[i-1]==EMPTY or (self._table[i-2]==EMPTY and self._table[i-1]==SHADOW)):
				print("bingo!!")
				x=i
				if self._table[i-2]==EMPTY:
					y=i-2
				else:
					y=i-1
				#swap!
				aux=self._table[x]
				self._table[x]=self._table[y]
				self._table[y]=aux
				#end swap :(
				self._iteration+=1
				if self.__is_finished():
					return False
				else:
					return True
		print("nope...")
		return False

	def __move_shadow(self):
		print("searching...")
		for i in range(0,(self._n_elem*2)):
			if (self._table[i]==SHADOW and ((self._table[i+1]==EMPTY) or (self._table[i+2]==EMPTY and self._table[i+1]==SUN))):
				print("bingo!!")
				x=i
				if self._table[i+2]==EMPTY:
					y=i+2
				else:
					y=i+1
				#swap!
				aux=self._table[x]
				self._table[x]=self._table[y]
				self._table[y]=aux
				#end swap :(
				self._iteration+=1
				if self.__is_finished():
					return False
				else:
					return True
		print("nope...")
		return False


	def solve(self):
		if self._n_elem==1:
			self._move_sun()
			self.print_table()
			self._move_shadow()
			self.print_table()
			self._move_sun()
			self.print_table()
			print("\tfinished!")
			return
		else:
			self.print_table()
			solved=False
			if not (self.__move_shadow()):
				self.print_table()
				return 0
			else:
				self.print_table()
				while not solved:

					if not (self.__move_sun()):
						self.print_table()
						return 0
					else:
						self.print_table()

					if not (self.__move_sun()):
						self.print_table()
						return 0
					else:
						self.print_table()

					if not (self.__move_shadow()):
						self.print_table()
						return 0
					else:
						self.print_table()

					if not (self.__move_shadow()):
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
