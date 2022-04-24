

from requests import delete


class User :
    """"
     my class which i will use to craeat new instances
     """
    user_list = []

    def __init__(self,name,password):
      self.name = name
      self.password  = password

    def save_user(self):
      """
       a method to save a new user to the list
       """

      User.user_list.append(self)
    
    @classmethod
    def show_user(cls):
        return cls.user_list

    def delete_user(self):
      """
      method to delete user from  the list
      """
      User.user_list.remove(self)


class Credentials:
    """
    Create credentials  class
    """
    credentials_list = []
    def __init__(self,account,name, password):
        """
        method that defines user credentials to be stored
        """
        self.account = account
        self.name = name
        self.password = password

    def save_datails(self):
        """
         a method to save the credentials
        """
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
         """
         delete the credentials method
         """
         