# Importing Credentials class

from password import Credentials

# Importing Userinfo class
from password import Userinfo


def create_userinfo(fname, lname, keypass):
    """
    function to create new user
    """
    new_userinfo = Userinfo(fname, lname, keypass)
    return new_userinfo


