import random
import string

# user_name =""
# user_password =""
global user_list
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