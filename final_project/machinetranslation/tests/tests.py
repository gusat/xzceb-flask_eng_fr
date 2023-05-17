import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    
    def test_englishToFrench_translation(self):
        english_text = 'Hello'
        expected_result = 'Bonjour'
        unexpected_result = 'Hello'
        result = english_to_french(english_text)
        self.assertEqual(result, expected_result)
        self.assertNotEqual(result, unexpected_result)

    def test_frenchToEnglish_translation(self):
        french_text = 'Bonjour'
        expected_result = 'Hello'
        unexpected_result = 'Bonjour'
        result = french_to_english(french_text)
        self.assertEqual(result, expected_result)
        self.assertNotEqual(result, unexpected_result)

    def test_englishToFrench_null_input(self):
        english_text = None
        expected_result = ''
        result = english_to_french(english_text)
        self.assertEqual(result, expected_result)

    def test_frenchToEnglish_null_input(self):
        french_text = None
        expected_result = ''
        result = french_to_english(french_text)
        self.assertEqual(result, expected_result)

 
if __name__ == '__main__':
    unittest.main()

