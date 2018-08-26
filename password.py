import string

import random

import pyperclip


class Userinfo:
    # 1.1 class variable to store created objects
    user_details = []

    # 1.2 method creating instances of Userinfo
    def __init__(self, first_name, last_name, passkey):
        # define properties for objects
        self.first_name = first_name
        self.last_name = last_name
        self.passkey = passkey

    # 1.3 method saving user info objects into user details list
    def save_userinfo(self):
        Userinfo.user_details.append(self)


class Credentials:
    # 2.1 class variable to store credentials
    credential = []

    # 2.5 creating list to display credentials
    show_credential = []

    # 2.2 creating instances of Credentials
    def __init__(self, user_name, service, password):

        # define properties for objects
        self.user_name = user_name
        self.service = service
        self.password = password

    # @classmethod
    # def check_userinfo(cls, first_name, last_name):
    #
    #     """
    #     checking user credentials
    #
    #     """
    #     current_userinfo = ""
    #
    #     for userinfo in Userinfo.user_details:
    #
    #         if userinfo.first_name == first_name and userinfo.last_name == last_name and userinfo.passkey == passkey:
    #             current_userinfo == userinfo.first_name
    #
    #     return current_userinfo

    # 2.3

    def save_credentials(self):
        """
        Method to save credential

        """
        Credentials.credential.append(self)

    # 2.4 generating random passwords

    def create_password(self, size=7, char=string.ascii_uppercase + string.ascii_lowercase + string.digits):
        """
        Generate random passwords function

        """
        paskey = ''.join(random.choice(char) for _ in range(size))
        return paskey

    # 2.6 show credentials of user
    # @classmethod
    # def show_credentials(cls, user_name):
    #     """
    #     method to show credentials of the user
    #
    #     """
    #     userinfo_show_credential = []
    #     for credential in cls.show_credential:
    #         if credential.user_name == user_name:
    #             userinfo_show_credential.append(credential)
    #     return userinfo_show_credential

    # 2.7 find service and return credentials
    @classmethod
    def find_by_service(cls, service):
        """
        method to find service and display credentials corresponding to service

        """
        for credential in cls.credential:
            if credential.service == service:
                return credential

    @classmethod
    def display_credentials(cls):
        return cls.credential
