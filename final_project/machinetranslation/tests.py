import unittest

from translator import englishToFrench, frenchToEnglish

class test_englishToFrench(unittest.TestCase) :
    def test1(self) :
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        
    


class test_frenchToEnglish(unittest.TestCase) :
    def test1(self) :
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        
    

unittest.main()