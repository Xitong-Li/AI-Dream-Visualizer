
import unittest
from ai_pipeline.text_utils import extract_keywords, get_emotion_category

class TestTextUtils(unittest.TestCase):

    def test_extract_keywords(self):
        text = "I dreamed of a golden castle floating in the sky."
        keywords = extract_keywords(text)
        self.assertIsInstance(keywords, list)
        self.assertTrue(len(keywords) > 0)

    def test_get_emotion_category(self):
        self.assertEqual(get_emotion_category(0.1, 0.5), "horror")
        self.assertEqual(get_emotion_category(0.5, 0.5), "fantasy")
        self.assertEqual(get_emotion_category(0.9, 0.5), "healing")

if __name__ == '__main__':
    unittest.main()
