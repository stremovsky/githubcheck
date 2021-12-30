import unittest
from check import check_status

class TestGithubCheck(unittest.TestCase):

  def test_check(self):
    try:
      check_status()
    except:
      self.fail("Exception in check_status")

if __name__ == '__main__':
    unittest.main()
