import unittest

class FirstTestCase(unittest.TestCase):
    def test_one(self):
        print("Run test_one...")
        pass

    def test_nota(self):
        print("Notatest runner....")
        pass

class SecondTestCase(unittest.TestCase):
    def test_two(self):
        print("Test_two running...")
        pass

    def test_two_part2(self):
        pass



if __name__ == '__main__':
    unittest.main()
