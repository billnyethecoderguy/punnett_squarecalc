class sgcell:
	g1 = 'A'
	g2 = 'a'
	repropool = []
	def __init__(self, ug1, ug2):
		if len(ug1) + len(ug2) > 2 or not isinstance(ug1, str) or len(ug1) + len(ug2) == 0 or not isinstance(ug2, str):
			raise Exception("A genotype must be a single character")
		self.g1 = ug1
		self.g2 = ug2
	def getgenes(self):
		return (self.g1, self.g2)
	def repro(self, othercell):
		if not isinstance(othercell, sgcell):
			raise Exception("Attempted to reproduce with non-cell")
		genpool = [[self.g1, othercell.g1], [self.g1, othercell.g2],
		           [self.g2, othercell.g1], [self.g2, othercell.g2]]
		self.repropool = [sgcell(*genpool[0]), sgcell(*genpool[1]),sgcell(*genpool[2]),sgcell(*genpool[3])]
		return (self.repropool)
	def __repr__(self):
		return f"[{self.g1}, {self.g2}]"
	def reprofancy(self, othercell):
		if not isinstance(othercell, sgcell):
			raise Exception("Attempted to reproduce with non-cell")
		genpool = [[self.g1, othercell.g1], [self.g1, othercell.g2],
		           [self.g2, othercell.g1], [self.g2, othercell.g2]]
		print(
		    f"|---------|\n| {genpool[0][0]}{genpool[0][1]} | {genpool[1][0]}{genpool[1][1]} |\n|---------|\n| {genpool[2][0]}{genpool[2][1]} | {genpool[3][0]}{genpool[3][1]} |\n|---------|")
cellbody = [sgcell('A', 'a'), sgcell('A', 'a')]
cellbody[0].reprofancy(cellbody[1])