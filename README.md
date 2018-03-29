#        password-locker

An application that allows us to generate and store passwords for various accounts.


## Created by [Christine Karimi ](https://github.com/christinekarimi)

## Description

An application that allows us to generate and store passwords for various accounts.
Password Locker stores a user's password for their various accounts. It also allows the user to generate random password and various credentials and stores them. This ensures that a user's password is strong enough and stored safely for easy retrieval.

## User Specifications

* In order to create an account with a user's details,log in and input password
* Store user,s login credentials
*Auto-generate a password for a new account

## Behaviours
| Behaviour | Input | Output |
| ------------ |:----------:| -------: | 
| Create user account | User_name: Puppah <br> Password: battousae| Hello Puppah, your account has been created |
| User Login|  User_name: Puppah <br> Password: battousae |  Welcome Puppah,how are you today?. What would you like to do? | 
| Create a Credential|Account name/ Site name: facebook <br> Site user_name: Govish <br> Site Password: 7kDzR6^l |New created account: <br> Account:facebook <br> User Name:Govish <br> Password:  7kDzR6^l |
| Display Credentials | DA| Site:Facebook <br> User Name:Govish <br> Password:7kDzR6^l|
| Genearate password or Enter existing passord|ep or gp  |Ep: Hakunapassword <br> or <br> gp: 7kDzR6^l |
| Exit Application | ex  | Come back again.......Goodbye!!|

## Installation
Clone this repo to a folder on your computer with

git clone  https://github.com/jonnygovish/password-locker.git

Run the run.py script to open the program.

## Technologies Used
* Python 3.6
## License
MIT (C) **[John Mutavi](https://github.com/jonnygovish)**
