# Importing Credentials class
#
import pyperclip
import sys
import random

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

def create_credentials(uname: object, servicename: object, access: object):
    """
    function to create credentials

    """
    new_credential = Credentials(uname, servicename, access)
    return new_credential


def save_credentials(credential):
    """
    function to save credentials

    """
    credential.save_credentials()


def display_credentials():
    """
    function to show credentials

    """
    return Credentials.display_credentials()


def find_credential(service):
    """
    function to find credential by service

    """
    return Credentials.find_by_service(service)


def check_across_credentials(service):
    """
    function to check if credentials exist with service

    """
    return Credentials.credential_exist(service)


def del_credentials(service):
    """
    function to delete credentials

    """
    Credentials.delete_credentials(service)


def copy_credentials(service):
    """
    function to copy credentials corresponding to service typed in
    :param service:
    :return:
    """
    return Credentials.copy_credentials(service)


def main():
    global uname, servicename, access, fname, lname, keypass, user_login
    print("Welcome Enter you Details")
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
    user_signup= (fname, lname, keypass)
    if user_signup == user_signup:
        print(f"Welcome {fname} {lname}, your details have been saved ")

        print("Type login to login ingot your account")

    short_code = input().lower()
    if short_code == 'login':
        print('Enter your firstname')
        first_name = input()
        print('Enter your last name')
        last_name = input()
        print('Enter your password')
        pass_word = input()

    user_exist = (first_name, last_name, pass_word)
    if user_signup != user_exist:
        print("login unsuccessful, wrong credentials")

        sys.exit()
    else:
        print(f"welcome {first_name} {last_name}, login successful")

    while True:
        print('\n')
        print("Type in Shortcode to choose preferred action: \n "
              "save - to create credentials, \n show - to display credentials, \n "
              "search -  to find by service, \n remove - to delete credentials, \n copy - to copy service password, "
              "\n exit -to exit app")

        short_code = input().lower()
        if short_code == 'save':

            print("Enter name: ")
            uname = input()

            print("Service Used: ")
            servicename = input()

            print("Your Password is: ")
            access = ''
            chars = "abcdefghijklmnopqrstuvwxyz1234567890!#.,?"
            access = ''.join(random.choice(chars)for _ in range(10))
            print(access, end='')

            save_credentials(create_credentials(uname, servicename, access))

        elif short_code == 'show':

            if display_credentials():
                print("Your stores credentials are: ")

                for credential in display_credentials():
                    print(f"username:{credential.user_name} \n service: {credential.service} \n password: {credential.password}")

            else:
                print('\n')
                print("No credentials saved")
                print('\n')

        elif short_code == 'search':

            print('Enter service to find credentials:')

            search_service = input()
            if check_across_credentials(search_service):
                search_credential = find_credential(search_service)
                print(f"Username:{search_credential.user_name} \n service: {search_credential.service} \n Password:"
                      f"{search_credential.password}")
            else:
                print("Credentials for service don't exist")

        elif short_code == 'remove':

            print("delete credential")

            search_service = input()
            if check_across_credentials(search_service):
                search_service = find_credential(search_service)
                del_credentials(search_service)
            else:
                print("credential doesn't exist")

        elif short_code == 'copy':
            print('')
            service_selected = input('Enter name of Service whose credentials you will copy ')
            copy_credentials(service_selected)
            print('')

            # else:
            #     print('No Credentials matching service')

        elif short_code == "exit":
            print(f"ADIOS {first_name} {last_name} ")

        else:
            print("wrong code")

        break


if __name__ == '__main__':
    main()
