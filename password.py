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

    def save_credentials(self):
        """
        Method to save credential

        """
        Credentials.credential.append(self)