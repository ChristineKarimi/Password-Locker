import string

class User:

  #This class creates new instances of the user
  

  user_list = [] #empty list
  def __init__(self, user_name, password,email):
    self.user_name = user_name
    self.password = password
    self.email = email
  


