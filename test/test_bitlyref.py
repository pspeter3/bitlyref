import unittest
import sys
sys.path.append('..')
import bitlyref

class TestBitlyRef(unittest.TestCase):
  def test_add_referrer(self):
    self.assertEqual('http://www.google.com?ref=python', 
      bitlyref.add_referrer('http://www.google.com', 'python'))

  def test_add_to_query_string(self):
    self.assertEqual('http://www.google.com?q=test&ref=python',
      bitlyref.add_referrer('http://www.google.com?q=test', 'python'))

  def test_change_parameter(self):
    self.assertEqual('http://www.google.com?trk=python', 
      bitlyref.add_referrer('http://www.google.com', 'python', param='trk'))

  def test_collision(self):
    self.assertRaises(Exception,
      bitlyref.add_referrer,
      'http://www.google.com?ref=fail',
      'python')

if __name__ == '__main__':
  unittest.main()