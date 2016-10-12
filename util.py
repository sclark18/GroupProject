import string
def remove_punct(text):
	""" 
	remove punctuation and non letters

	>>> remove_punct("yo")
	'yo'

	>>> remove_punct("Hello There!")
	'Hello There'

	>>> remove_punct("money££££")
	'money'
	"""
	output = ""
	for c in text:
		if c in string.ascii_letters or c in string.whitespace:
			output += c
	return output

def normalize(text):
	"""
	returns a list of words in lower case:
	
	>>> normalize("abcdefg")
	['abcdefg']

	>>> normalize("Hello There")
	['hello', 'there']

	>>> normalize("iS thIS w0rKinG??")
	['is', 'this', 'wrking']
	
	"""

	no_punct = remove_punct(text)
	no_punct = no_punct.lower()
	output = str.split(no_punct)
	return output

def filter(words, skip_words):
	"""
	filters a list of words, removing unnecessary words

	>>> filter(['testing'], ['testing'])
	[]

	>>> filter(['one', 'two', 'three'], ['two'])
	['one', 'three']
	"""
	output = []
	for w in words:
		if w not in skip_words:
			output.append(w)
	return output




