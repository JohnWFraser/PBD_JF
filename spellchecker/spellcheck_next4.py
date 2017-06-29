class SpellChecker:
	def __init__(self):
		self.words = []
	def load_words(self, file_name):
		self.words = open(file_name).readlines()
		self.words = map(lambda x: x.strip(), self.words)
#		return words
	def check_word(self, word):
		return word.strip('.').lower() in self.words
		#return word in self.words
		
	def check_words(self, sentence):
		words_to_check = sentence.split(' ')
		failed_words = []
		for word in words_to_check:
			if not self.check_word(word):
				print('Word is misspelt : ' + word)
				failed_words.append(word)#return False
		return failed_words#return True

if __name__ == '__main__':
    spellChecker = SpellChecker()
    spellChecker.load_words('spell.words')
    print(spellChecker.check_word('zygotic'))
    print(spellChecker.check_words('zygotic mistasdas elementary'))
	