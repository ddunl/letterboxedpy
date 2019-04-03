import sys, time

class board:
	def __init__(self, puzzStr, filename = "modWords2.txt"):
		if len(puzzStr) != 12:
			raise Exception("Length of puzzle is invalid. Length of puzzle was: {}".format(len(puzzStr)))

		self.puzzDict = {i:-1 for i in "abcdefghijklmnopqrstuvwxyz"}#could use a default dict for this but this is fine

		for i, letter in enumerate(puzzStr):
			self.puzzDict[letter] = i/3 #dict where letter corresponds to side number

		self.filename = filename

		self.spanningSet = set([i for i in puzzStr])

	def validWord(self, word): #check if word is playable
		last = -1
		for letter in word:
			side = self.puzzDict[letter]
			if side == -1:
				return False
			else:
				if side == last:
					return False
				else:
					last = side
		else:
			return True

	def checkWordList(self, cutoff = 2): #check file to find all valid words
		temp = []
		with open(self.filename) as wordList:

			for word in wordList:
				if self.validWord(word[:-cutoff]):
					temp.append(word[:-cutoff])
		
		temp.sort(key = len, reverse = True)
		self.possWords = temp
		
		return 


	def isSolution(self, arr): #decide if something is solution
		allLetters = set()

		for word in arr:
			for letter in word:
				allLetters.add(letter)

		if allLetters == self.spanningSet:
			return True

		return False


	def findSolutions(self):
		temp = []
		counter = 0
		for word in self.possWords:
			for word2 in self.possWords:
				if self.isSolution([word, word2]):
					if word[-1] == word2[0]:
						counter += 1
						temp.append([word, word2])
		self.solutions = temp
		return
						

	def solve(self, sortby = ""):

		self.checkWordList()
		print "Found all valid words... ({})".format(len(self.possWords))

		self.findSolutions()
		print "Found all solutions... ({})".format(len(self.solutions))


		if sortby == "shortest":
			self.solutions.sort(key = lambda x: len(x[0]) + len(x[1]))
		
		elif sortby == "alpha":
			self.solutions.sort()

		else:
			self.solutions.sort(key = lambda x: len(x[0]) + len(x[1]), reverse = True)

		for i, sol in enumerate(self.solutions):
			print "{}. {} {}".format(i, sol[0], sol[1])
		
  

start = time.time()

if len(sys.argv) == 2:
	board(sys.argv[1]).solve()

elif len(sys.argv) == 3:
	board(sys.argv[1].solve(sortby = sys.argv[2]))

print "Took {} seconds".format(time.time() - start)
