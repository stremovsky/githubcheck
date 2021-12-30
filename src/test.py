import unittest
from check import check_status

class TestGithubCheck(unittest.TestCase):

  def test_check(self):
    self.assertRaises(Exception, check_status)

if __name__ == '__main__':
    unittest.main()
