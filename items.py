import random
class Equipment:
	def __init__(self, val, weight, namelist, addlist, type):
		self.val = val
		self.weight = weight
		i = random.randrange(0,len(namelist))
		j = random.randrange(0,len(addlist))
		self.name = addlist[j] + " " + namelist[i]
		self.type = type
	
	def get_full_name(self):
		return self.name + " (+" + str(self.val) + " " + self.type + ")"
class Potion:
	def __init__(self, tier, type):
		self.type = type
		self.val = tier * 5
		self.name = type + " Potion"

	def get_full_name(self):
		return self.name + " (+" + str(self.val) +")"

