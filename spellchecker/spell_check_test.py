import unittest
from spellcheck_next4 import SpellChecker

class TestSpellChecker(unittest.TestCase):

    def setUp(self):
		self.spellChecker = SpellChecker()
		self.spellChecker.load_words('spell.words')

    def test_spell_checker(self):
		self.assertTrue(self.spellChecker.check_word('zygotic'))
		failed_words = self.spellChecker.check_words('zygotic mistasdas elementary')
		self.assertEquals(1, len(failed_words))
		self.assertEquals('mistasdas', failed_words[0])
		self.assertEquals(0, len(self.spellChecker.check_words('our first correct sentence')))
        # handle case sensitivity
		self.assertEquals(0, len(self.spellChecker.check_words('Our first correct sentence')))
        # handle full stop
		self.assertEquals(0, len(self.spellChecker.check_words('Our first correct sentence.')))
		failed_words = self.spellChecker.check_words('zygotic mistasdas spelllleeeing elementary')
		self.assertEquals(2, len(failed_words))
		self.assertEquals('mistasdas', failed_words[0])
		self.assertEquals('spelllleeeing', failed_words[1])
# more bugs because the spell checker doesnt spell check itself correctly (21 entries not correct) dictionary words need to be lower
#		self.assertEqual(21, len(self.spellChecker.check_document('spell.words')))
		self.assertEqual(0, len(self.spellChecker.check_document('spell.words')))


if __name__ == '__main__':
    unittest.main()
