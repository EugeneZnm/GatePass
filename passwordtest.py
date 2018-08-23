# 1 importing unittest module

import unittest

# 2 import Userinfo class

from userinfo import Userinfo


# 3 subclass TestUserinfo inheriting from unittest.Testcase
class TestUserinfo(unittest.TestCase):

    # 4 setup method to run before each testcase
    def setUp(self):

        # 5 creating new Userinfo object
        self.new_userinfo = Userinfo("", "", "")

