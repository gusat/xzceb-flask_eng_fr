import unittest
from translatev2 import englishToFrench, frenchToEnglish

class TestTranslation(unittest.TestCase):
    def test_englishToFrench_null(self):
        self.assertIsNone(englishToFrench(None))

    def test_frenchToEnglish_null(self):
        self.assertIsNone(frenchToEnglish(None))

    def test_englishToFrench_hello(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")

    def test_frenchToEnglish_bonjour(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")

if __name__ == '__main__':
    unittest.main()
    
