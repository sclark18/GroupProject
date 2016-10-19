import random
class Equipment:
	def __init__(self, val, namelist, addlist, type):
		self.val = val
		addlen = len(addlist)
		namelen = len(namelist)
		j = random.randrange(0,addlen)
		i = random.randrange(0,namelen)
		self.name = addlist[j].title() + " " + namelist[i]
		self.type = type
	
	def get_full_name(self):
		return self.name + " (+" + str(self.val) + " " + self.type + ")"
class Potion:
	def __init__(self):
		self.val = 5
		self.name = "Health Potion"
		self.colour = "\033[1;34;40m"

	def get_full_name(self):
		return "Health Potion"

