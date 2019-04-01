caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def noRepeats(str1):
	temp = ""
	for i in str1:
		if i in temp:
			return False
		else:
			temp += i
	
	return True	

with open("words.txt") as dictFile:
	with open("modWords.txt", "w") as newDictFile:
		for line in dictFile:
			if line[0] in caps:
				pass
			elif noRepeats(line) and line[:-1].isalpha() and line[:-1].islower():
				newDictFile.write(line)


		

with open("modWords.txt") as newDictFile:
	for index, line in enumerate(newDictFile):
		print index



