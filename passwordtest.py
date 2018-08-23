# 1 importing unittest module

import unittest

# 2 import Userinfo class

from password import Userinfo


# 3 subclass TestUserinfo inheriting from unittest.Testcase
class TestUserinfo(unittest.TestCase):

    # 4 setup method to run before each testcase
    def setUp(self):

        # 5 creating new Userinfo object
        self.new_userinfo = Userinfo("Genghis", "Khan", "chingis@gmail.com")

    # 6 Test for proper object initialisation
    def test__init(self):
        self.assertEqual(self.new_userinfo.first_name, "Genghis")
        self.assertEqual(self.new_userinfo.last_name, "Khan")
        self.assertEqual(self.new_userinfo.email, "chingis@gmail.com")

if __name__ == '__main__':
    unittest.main()

