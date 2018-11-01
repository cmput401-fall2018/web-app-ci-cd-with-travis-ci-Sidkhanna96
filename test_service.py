import unittest
from unittest.mock import patch
from unittest import TestCase


import service

class test_service(TestCase):
    @patch('service.Service.bad_random')
    def test_bad_random(self, mock_bad_random):
        i = 1
        mock_bad_random.return_value = i
        br = service.Service()
        result = br.bad_random()
        self.assertEqual(result, i)

    @patch('service.Service.bad_random')
    def test_divide(self, mock_bad_random):
        i = 5
        mock_bad_random.return_value = i
        br = service.Service()
        result2 = br.divide(2)
        test = 2.5
        self.assertEqual(test, result2)

    @patch('service.Service.bad_random')
    def test_abs_plus(self, mock_bad_random):
        i = 5
        mock_bad_random.return_value = i
        br = service.Service()
        result2 = br.abs_plus(2)
        test = 3
        self.assertEqual(test, result2)


    @patch('service.Service.bad_random')
    def test_complicated_function(self, mock_bad_random):
        i = 5
        mock_bad_random.return_value = i
        br = service.Service()
        result2 = br.complicated_function(2)
        test = (2.5, 1)
        self.assertEqual(test, result2)

if __name__ == '__main__':
  unittest.main()