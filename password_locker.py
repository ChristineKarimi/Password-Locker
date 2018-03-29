import random
import string

class User:
  """
  Class that generates new instances of user
  """

  user_list = [] #empty user list
  def __init__(self, user_name, password,email):
    self.user_name = user_name
    self.password = password
    self.email = email
  
  def user_save(self):
    """
    saves user object into user object.
    """
    User.user_list.append(self)
  @classmethod
  def display_users(cls):
    return cls.user_list

  class Credentials:
  """
  Class that generates new instances of credential object.
  """
  global user_list
  credential_list =[]
  def __init__(self, account_name, account_username, account_password):
    self. account_name = account_name
    self.account_username = account_username
    self.account_password = account_password
  @classmethod
  def check_user_exist(cls,user_name,password):
    """
    Method that checks if a user exist from user list.
    """
    for user in User.user_list:
      if user.user_name == user_name and user.password == password:
        return True
      return False