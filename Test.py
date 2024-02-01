import unittest

from Prog import summation

class TestSum(unittest.TestCase):
  def test_list_int(self):
    data = [69, 420]
    result = summation(data)
    self.assertEqual(result, 489)

if __name__ == '__main__':
  unittest.main()
    
