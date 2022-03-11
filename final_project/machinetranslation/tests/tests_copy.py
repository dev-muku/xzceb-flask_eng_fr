import unittest

from translator import english_to_french, french_to_english

class test_english_to_french(unittest.TestCase) :
    def test1(self) :
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        
    def test2(self) :
        self.assertIsNone(english_to_french(None), 'Not none')


class test_french_to_english(unittest.TestCase) :
    def test1(self) :
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        
    def test2(self) :
        self.assertIsNone(french_to_english(None), 'Not none')

unittest.main()