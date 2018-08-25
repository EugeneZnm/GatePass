# Importing Credentials class

import pyperclip

from password import Credentials

# Importing Userinfo class
from password import Userinfo


def create_userinfo(fname, lname, keypass):
    """
    function to create new user
    """
    new_userinfo = Userinfo(fname, lname, keypass)
    return new_userinfo


def save_userinfo(userinfo):
    """
    function to save contacts

    """
    userinfo.save_userinfo()


# CREDENTIALS FUNCTIONS

def create_credentials(uname, servicename, access):
    """
    function to create credentials

    """
    new_credential = Credentials(uname, servicename,access)
    return new_credential

def main():
    print("Welcome Enter you Details")
    while True:
        print("Type in Shortcode to choose preferred action:"
              "start - to enter user details,  save - to create credentials, gen - to generate random password")

        short_code = input().lower()
        if short_code == "start":
            print(" Enter User Info")

            print("First Name:.")
            fname = input()

            print("Last Name:.")
            lname = input()

            print("Enter password: ")
            keypass = input()

            """
            Create and save contacts
            """
            print('\n')
            save_userinfo(create_userinfo(fname, lname, keypass))
            print(f"Welcome {fname} {lname}, your details have been saved ")
            print('\n')

        elif short_code == 'save':




if __name__ == '__main__':
    main()
