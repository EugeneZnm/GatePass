# 1 importing unittest module

import unittest

# import pyperclip

import pyperclip

# 2 import Userinfo class

from password import Userinfo


# 3 subclass TestUserinfo inheriting from unittest.Testcase
class TestUserinfo(unittest.TestCase):

    # 4 setup method to run before each testcase
    def setUp(self):
        # 5 creating new Userinfo object
        self.new_userinfo = Userinfo("Genghis", "Khan", "qwer1234.")

    # 6 Test for proper object initialisation
    # TEST 1
    def test__init(self):
        self.assertEqual(self.new_userinfo.first_name, "Genghis")
        self.assertEqual(self.new_userinfo.last_name, "Khan")
        self.assertEqual(self.new_userinfo.passkey, "qwer1234.")

    # 7 TEST 2 test if user info object is saved into user details list
    def test_save_details(self):
        self.new_userinfo.save_details()
        self.assertEqual(len(Userinfo.user_details), 1)

class TestCredentials(unittest.TestCase):

    """
    Test class defining test cases for Credentials class behaviours

    """

    def setUp(self):
        """
        Testing proper object initialisation
        """
        self.new.credentials = Credentials()


if __name__ == '__main__':
    unittest.main()
