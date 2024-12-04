import itertools
def hnn(string):
	for char in string:
		if char.isdigit() or not char.isalpha():
			return True
	return False
def isvalid(a):
	if hnn(a):
		return False
	counter = 0
	vl = 0
	for letter in a:
		if counter % 2 == 1:
			continue
		elif a[counter + 1].lower() == letter.lower():
			vl += 2
	if vl == len(a):
		return True
	else:
		return False
class mgcell():
	genome = ""
	def __init__(self, alleles):
		if not isvalid(alleles):
			raise Exception("invalid alleles")
		self.genome = [alleles[:2], alleles[2:]]
	def getgenes(self):
		return (self.genome)
	def repro(self, othercell):
		if not isinstance(othercell, mgcell):
			raise Exception("Attempted to reproduce with non-cell")
		combolist = list(itertools.product(*self.genome))
		combolist2 = list(itertools.product(*othercell.genome))
		punnett_square = []
		for parent1_comb in combolist:
			for parent2_comb in combolist2:
				offspring = ''.join(
				    sorted(parent1_comb[0] + parent2_comb[0])) + ''.join(
				        sorted(parent1_comb[1] + parent2_comb[1]))
				punnett_square.append(offspring)
		unique_offspring = sorted(set(punnett_square))
		return (unique_offspring)
cellbody = [mgcell("AaBb"), mgcell("AaBb")]
print(cellbody[0].repro(cellbody[1]))