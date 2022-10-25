import unittest
import translator

class Testing(unittest.TestCase):
    def test_e2f(self):
        self.assertEqual(translator.english_to_french('Hello'), 'Bonjour')
        self.assertRaises(Exception, translator.english_to_french, "")

    def test_f2e(self):
        self.assertEqual(translator.french_to_english("Bonjour"), "Hello")
        self.assertRaises(Exception, translator.french_to_english, "")

if __name__ == '__main__':
    unittest.main()
    