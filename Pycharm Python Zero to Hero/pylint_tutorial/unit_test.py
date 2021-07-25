import unittest
import tutorial1


class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = tutorial1.cap_text(text)
        self.assertEqual(result, 'Python')


if __name__ == '__main__':
    unittest.main()
