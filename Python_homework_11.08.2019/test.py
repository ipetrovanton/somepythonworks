import unittest
import run


class Test(unittest.TestCase):
    def setUp(self):
        print('start')

    def test_numbers1(self):
        self.assertEqual(run.get_lucky([56, 78, 123, 7, 0]), [78, 7])

    def test_numbers2(self):
        self.assertEqual(run.get_lucky([777, 78, 123, 7, 0]), [777, 78, 7])

    def test_numbers3(self):
        self.assertEqual(run.get_lucky([0, 0, 0, 0, 0]), [])

    def tearDown(self):
        print('end')


if __name__ == '__main__':
    unittest.main()
