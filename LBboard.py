class board:
	def __init__(self, puzzStr, filename = "modWords.txt"):
		if len(puzzStr) != 12:
			raise Exception("Length of puzzle is invalid. Length of puzzle was: {}".format(len(puzzStr)))
		self.puzzDict = {i:-1 for i in "abcdefghijklmnopqrstuvwxyz"}
		for i, letter in enumerate(puzzStr):
			self.puzzDict[letter] = i/3
		print self.puzzDict

		self.filename = filename

	def validWord(self, word):
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

	def checkWordList(self):
		with open(self.filename) as wordList:
			for word in wordList:
				if self.validWord(word[:-1]):
					print word[:-1]




b = board("emlakustbocr")
print b.validWord("laces")

b.checkWordList()