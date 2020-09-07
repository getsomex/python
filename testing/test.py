import unittest
import script


class TestMain(unittest.TestCase):
    def setUp(self):
        print('aboout to test a function')

    def test_do_stuff(self):
        '''
        hi
        '''
        test_param = 10
        result = script.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'sshkhs'
        result = script.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = script.do_stuff(test_param)
        self.assertEqual(result, 'please enter a number')

    def tearDown(self):
        print('cleaning up')


if __name__ == '__main__':
    unittest.main()
