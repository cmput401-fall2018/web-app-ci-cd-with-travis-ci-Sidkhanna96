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
    # @patch('service.Service.abs_plus')
    # def test_abs_plus(self, mock_abs_plus):
    #     i = 5
    #     mock_abs_plus.return_value = i
    #     bap = service.Service()
    #     result = bap.abs_plus(5)
    #     self.assertEqual(result, i)

    # @patch('service.Service.complicated_function')
    # def test_complicated_function(self, mock_complicated_function):
    #     i = 5
    #     mock_complicated_function.return_value = i
    #     bcf = service.Service()
    #     result = bcf.complicated_function(5)
    #     self.assertEqual(result, i)

if __name__ == '__main__':
  unittest.main()