import unittest
from to_roman import to_roman, NonValidInput


class Test(unittest.TestCase):
    def setUp(self):
        print('start')

    def test_numbers1(self):
        self.assertEqual(to_roman(505), "D V")

    def test_numbers2(self):
        self.assertEqual(to_roman(10), "X")

    def test_numbers3(self):
        self.assertEqual(to_roman(999), "CM XC IX")

    def test_numbers4(self):
        self.assertEqual(to_roman(4444), "MMMM CD XL IV")

    def test_numbers5(self):
        self.assertEqual(to_roman(4470), "MMMM CD LXX")

    def test_numbers6(self):
        self.assertEqual(to_roman(1), "I")

    def test_number7(self):
        self.assertRaises(NonValidInput, to_roman, -1)
        self.assertRaises(NonValidInput, to_roman, -13284234)

    def test_number8(self):
        self.assertRaises(NonValidInput, to_roman, 0)

    def test_number9(self):
        self.assertRaises(NonValidInput, to_roman, 5000)
        self.assertRaises(NonValidInput, to_roman, 5009080)

    def test_number10(self):
        self.assertRaises(NonValidInput, to_roman, "kakayato stringa!")

    def tearDown(self):
        print('end')


if __name__ == '__main__':
    unittest.main()
