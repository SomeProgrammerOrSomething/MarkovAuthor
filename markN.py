def markN(corpus):

	# This is my Markovian N-degree Text Generator

	# Is it really a Markovian Cocktail Party without Randomness?
	import random

	# Ask for n_degree & word count.

	# Things to fix, this code needs to be adapted for better choices & errors.
	# For better input collection use raw_input & conditionals

	n_degree = int( raw_input("What is the Markovian degree for approximation?: ") )
	word_count = int( raw_input("About how many words do you want the generated text to have?: ") )
	word_count = word_count/n_degree

	# Make into a function for DRY SW:
	def length(text):
		# Length Calculation
		length = 0;
		for word in text:
			length = length + 1
		return length

	# Ensure Corpus is a List:
	def stringToList(text):
		# Check if String
		if type(corpus) == type(''):
			word_bank = corpus.split()
		elif type(corpus) == type([]):
			word_bank = corpus
		else:
			print ("This program requires a string as input.")
			quit()
		return word_bank

	# This section helps with the mathematical generations.
	# Consider xrange or range.
	
	### Take Corpus as string and convert to list
	base = stringToList(corpus)

	### Record the length of base (the new list), then
	### subtract n_degree so that we can properly capture
	### the different n-grams in the base

	length = length(base)
	length = length - n_degree


	# Begin Story as Empty List, then add n-grams on.
	story = "\n\n"

	for word_index in range(word_count):
		# Pick a random location within the n-gram space of 
		# the base
		start_index = random.randint(0, length )

		# While keep concatenating n-grams onto the story
		# until the desired story's length is reached.
		for degree_index in range(n_degree):
			story = story + " " + base[start_index+degree_index]

	print story

file = open('pym.txt','r')
corpus = file.read()
markN(corpus)