from unittest import TestCase
from urlsplit2 import Urlsplit
__author__ = 'SWarren'


class TestUrlsplit(TestCase):
    def test_error_no_HTTP_HTTPS(self):
        HttpTest = Urlsplit().SplitIntoList('www.makeit.org/demo/appl?input=3')
        self.assertEqual(HttpTest,'error in input',msg='not equal')
        print('Testing the address www.makeit.org/demo/appl?input=3')
        print('Error No HTTP:// or HTTPS:// Test Sucessful')
        print('')

    def test_Correct_Address(self):
        HttpTest = Urlsplit().SplitIntoList('http://www.makeit.org/demo/appl?input=3')
        actualTest = ['http', 'www.makeit.org', '/demo/appl', 'input=3']
        self.assertEqual(HttpTest,actualTest,msg='not equal')

        print('Testing the address http://www.makeit.org/demo/appl?input=3')
        print('Correct Address Test Successful')
        print('')

    def test_Garabage(self):
        HttpTest = Urlsplit().SplitIntoList('loveyourcouch.com/rich')
        '''actualTest = ['http', 'www.makeit.org', '/demo/appl', 'input=3']'''
        print(HttpTest)

        self.assertEqual(HttpTest,'error in input',msg='not equal')
        print('Testing loveyourcouch.com/rich ')
        print('Garabage Test Successful')
        print('')




    def test_new(self):

        print('The Tests have been Completed')


