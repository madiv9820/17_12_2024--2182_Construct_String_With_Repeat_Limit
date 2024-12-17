from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testCases = {1: ('cczazcc', 3, 'zzcccac'), 2: ('aababab', 2, 'bbabaa')}
        self.__obj = Solution()
        return super().setUp()
    
    @timeout(0.5)
    def test_case_1(self):
        s, repeatLimit, output = self.__testCases[1]
        result = self.__obj.repeatLimitedString(s = s, repeatLimit = repeatLimit)
        self.assertIsInstance(output, str)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_case_2(self):
        s, repeatLimit, output = self.__testCases[2]
        result = self.__obj.repeatLimitedString(s = s, repeatLimit = repeatLimit)
        self.assertIsInstance(output, str)
        self.assertEqual(result, output)

if __name__ == '__main__': unittest.main()