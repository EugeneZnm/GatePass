# 1 importing unittest module

import unittest

# 2 import Userinfo class

from password import Userinfo

from password import Credentials


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
    def test_save_userinfo(self):
        self.new_userinfo.save_userinfo()
        self.assertEqual(len(Userinfo.user_details), 3)

    def test_save_multiple_userinfo(self):
        """
        testing to save multiple user details

        """
        self.new_userinfo.save_userinfo()
        test_userinfo = Userinfo("Genghis", "Khan", "qwer1234.")
        test_userinfo.save_userinfo()
        self.assertEqual(len(Userinfo.user_details), 2)



class TestCredentials(unittest.TestCase):
    """
    Test class defining test cases for Credentials class behaviours

    """

    # def test__check__userinfo(self):
    #     """
    #     Test if user credentials are matching
    #
    #     """
    #     self.new_userinfo == Userinfo("Genghis", "Khan", "qwer1234.")
    #     self.new_userinfo_save_details()
    #
    #     for userinfo in Userinfo.user_details:
    #
    #         if new_userinfo.first_name == userinfo.first_name and new_userinfo.last_name == userinfo.last_name and new_userinfo.passkey == userinfo.passkey
    #                 return current_userinfo
    #     self.assertEqual(current_userinfo, Credentials(check_userinfo(user2.password, user2.email))

    def setUp(self):
        """
        Testing proper object initialisation in credential class

        """
        self.new_credential = Credentials("Eugene znm", "whatsapp", "123ert")

    def test__init(self):
        """
        checking for expected results

        """
        self.assertEqual(self.new_credential.user_name, "Eugene znm")
        self.assertEqual(self.new_credential.password, "123ert")
        self.assertEqual(self.new_credential.service, "whatsapp")

    def test__save__credentials(self):

        """
        Test saving of single set of credentials

        """
        self.new_credential.save_credentials()
        self.assertEqual(len(Credentials.credential), 1)

    def test__save__multiple__credentials(self):

        """
        Test for saving of multiple credentials

        """
        self.new_credential.save_credentials()
        test_credential = Credentials("Eugene znm", "whatsapp", "123ert")
        test_credential.save_credentials()
        self.assertEqual(len(Credentials.credential), 2)

    def tearDown(self):
        """
        functions to clear credentials after every test

        """
        Credentials.credential = []
        Userinfo.user_details = []

    def test_show_credentials(self, user_name=None):
        """
        testing display of correct credentials
        :return: 
        """
        self.new_credential.save_credentials()

        self.assertEqual(len(Credentials.show_credentials(user_name)), 0)
        
        
        
if __name__ == '__main__':
    unittest.main()
