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

    # 1.4 verification
    # def check(self, first_name, last_name, passkey):
    #     print(self.first_name)
    #     if self.first_name == first_name and self.last_name == last_name and self.passkey == passkey:
    #         print ("success")


class Credentials:
    # 2.1 class variable to store credentials
    credentiall = []

    # 2.5 creating list to display credentials
    # show_credential = []

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
        Credentials.credentiall.append(self)

    # def save_multiple(self):


    # 2.4 generating random passwords

    # def create_password(self, size=7, char=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    #     """
    #     Generate random passwords function
    #
    #     """
    #     paskey = ''.join(random.choice(char) for _ in range(size))
    #     return paskey

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
        for credential in cls.credentiall:
            if credential.service == service:
                return credential

    # 2.8
    @classmethod
    def credential_exist(cls, service):
        """
        check if credential exists from credential list
        """
        for credential in cls.credentiall:
            if credential.service == service:
                return True
            return False

    # 2.9
    @classmethod
    def display_credentials(cls):
        """
        method to display credentials
        :return:
        """
        return cls.credentiall

    # 2.10
    def delete_credentials(self):
        """
        method to delete credentials
        :return:
        """
        Credentials.credentiall.remove(self)

    # 2.11
    @classmethod
    def copy_credentials(cls, service):
        """
        method to copy credential information after credential's service is called
        :param service:
        :return:
        """
        find_credential = Credentials.find_by_service(service)
        pyperclip.copy(find_credential.password)