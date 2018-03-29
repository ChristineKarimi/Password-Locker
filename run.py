#!/usr/bin/env python3.6

from password_locker import User, Credentials

def create_user(user_name, password, email):
  """
  Function to create a new user.
  """
  new_user = User(user_name,password, email)
  return new_user

  def save_user(user):
  """
  Function to save user.
  """
  user.user_save()
def display_users():
   return User.display_users()
  
  def login_user(user_name,password):
  """
  function that checks whether a user exist and then login the user in.
  """
  check_user_exist = Credentials.check_user_exist(user_name,password)
  return check_user_exist

  def create_credential(account_name,account_username, account_password):
  """
  Function to create a new credential.
  """
  new_credential = Credentials(account_name,account_username,account_password)
  return new_credential