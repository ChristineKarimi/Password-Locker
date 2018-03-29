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

  def save_credential(credential):
  """
  Function to save new  credential.
  """
  credential.save_account()

  def delete_account(credential):
  """
  Function to delete a credential.
  """
  credential.delete_account()

  def display_accounts():
  """
  Function that returns all the saved credential.
  """
  return Credentials.display_accounts()

 def generate_password():
  """
  Function that generates random password.
  """
  password_gen = Credentials.generate_password()

  return password_gen 

 def main():
  print("This is Password Locker")
  print('\n')
  while True:
    print('.'* 60)  
    short_code = input("Use this short codes: CU- create a new user account, LN - login into your account (if you already have a password locker account), EX - exit from password locker \n").lower().strip()
    print('.'* 60)
    
    if short_code == "ex":
        print("See yah again.......Goodbye!!")
        break 

        elif short_code == "cu":
        print("Sign Up")
        print('-' * 30)
        user_name = input("User_name: ")
        password = input("Password: ")
        email = input("Email: ")
        
        save_user(create_user(user_name,password,email))
        print('\n')
        
        print(f"Hello,{user_name} your account has been created")
        print('\n')
        print('-' * 30)

        elif short_code == "d":
        if display_users():
            print("Here's a list of the users:")
            print('\n')
            for user in display_users():
                print(f"{user.user_name}")
                print('\n')
        else:
            print("There are no users saved yet")


    elif short_code == "ln":
        print("Please Enter your Username and your Password to log in")
        print('-' * 30)
        user_name = input("Username: ")
        password = input("password: ")
        sign_in = login_user(user_name,password)
        if sign_in == True:
            print(f"Hi,{user_name},What would you like to do?")
            while True:
                print('.'* 60)
                short_code = input("Codes: CA - create an account or name of the site your want, DA- display the list of your accounts or sites, EX- exit the site \n").lower().strip()
                print('.'* 60)
                if short_code == "ca":
                    print("Create new credentials")
                    print('*' * 30)
                    account_name = input("Account name/ Site name: ")
                    account_username = input("Site User Name: ")
                    print('.'* 60)
                    password_option = input("Please choose between: (ep-enter existing password) or (gp-generate new password) \n").strip()
                    print('.'* 60)
                    while True:
                        if password_option == "ep":
                            account_password = input("Enter your password (minimum 8 characters): ")
                            break
                        elif password_option == "gp":
                            account_password = generate_password()
                            break
                        else:
                            print("Invalid option")
                            break
                    save_credential(create_credential(account_name,account_username,account_password))
                    print('*' * 30)
                    print(f"New created account: \n Account:{account_name}\n User Name:{account_username} \n Password: {account_password}")
                    print('*' * 30)
    
                elif short_code == "da":
                    if display_accounts():
                        print("Here's your list of acoount(s): ")
                        
                        print('#' * 30)
                        for account in display_accounts():
                            print(f" Site:{account.account_name} \n User Name:{account_username}\n Password:{account_password}")
                            print('_'* 30)
                        print('#' * 30)
                    else:
                        print("No accounts yet")
                        
                elif short_code == "ex":
                    print("See you again!!!!")
                    break
                else:
                    print("Invalid Choice")
                    
                         
                    
#                break
                
        else:
            print("Ooops!You dnt have an account. To proceed please create an account.")
            
#    break
    



if __name__ == '__main__':
  main()