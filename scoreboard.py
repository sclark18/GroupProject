def process_file(address):
	# loads scores into memory
	try:
		f = open(address, 'r')
	except FileNotFoundError:
		open(address, 'w')
		f = open(address,'r')
	spl = f.read()
	format = str.split(spl, "\n")
	name = []
	score = []
	data = [name, score]
	if len(format) > 0:
		for index, i in enumerate(format):
			split = str.split(format[index], ',')
			if len(split) < 2:
				break
			name.append(split[0])
			score.append(int(split[1]))
	return data

def add_score(data, score,name):
	for index, i in enumerate(data[0]):
		if score > data[1][index]:
			data[1].insert(score,index)
			data[0].insert(score,index)
			return data
	data[1].append(score)
	data[0].append(name)
	return data

def save_data(address,data, score, name):
	f = open(address, 'w')
	sdata = add_score(data, score, name)
	for index, i in enumerate(sdata[0]):
		f.write(str(sdata[0][index]) + "," + str(sdata[1][index]))
		if index != len(sdata[0]) - 1:
			f.write("\n")
	f.close()


def print_scoreboard(data):
	for index, i in enumerate(data[0]):
		print(str(index + 1) + "." + data[0][index] + ": " + str(data[1][index]))
"""
names = ["Sam","Sam2","Sam3"]
scores = [25,15,5]
chk = [names,scores]
print_scoreboard(chk)
"""