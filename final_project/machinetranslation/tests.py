import unittest
from translator import english_to_french, french_to_english

class Testenglish_to_french(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french(""), "NO INPUT PROVIDED.") # Test when input is null or empty
        self.assertEqual(english_to_french("Hello"), "Bonjour") # test when input is "Hello"

class Testfrench_to_english(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english(""), "NO INPUT PROVIDED.") # test when input is null or empty
        self.assertEqual(french_to_english("Bonjour"),"Hello") # test when input is "Bonjour"

unittest.main()
