import unittest
from translator import english_to_french
from translator import french_to_english

class Testenglish_to_french(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(english_to_french('None'),"")  # Test for null input for englishToFrench.
        self.assertEqual(english_to_french('Hello'),'Bonjour') # Test for the translation of the world 'Hello' and 'Bonjour'
        
class Testfrench_to_english(unittest.TestCase): 
    def test2(self): 
        self.assertNotEqual(french_to_english('None'),"")  # Test for null input for frenchToEnglish.
        self.assertEqual(french_to_english('Bonjour'),'Hello' ) # Test for the translation of the world 'Bonjour' and 'Hello'.
     
unittest.main()