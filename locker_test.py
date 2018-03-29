import unittest
from password_locker import User

class TestUser(unittest.TestCase):

    #Test that defines test cases for the user class bevaviours
    
    def setUp(self):
        """
        set up method to run before each test cases
        """
        self.new_user = User("kim", "5991", "karimikim3@gmail.com")
    def test_init(self):
        """
        Test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_user.user_name,"kim")
        self.assertEqual(self.new_user.password, "5991")
        self.assertEqual(self.new_user.email, "karimikim3@gmail.com")


    def tearDown(self):
        """
        Method that cleans up after each case has run.
        """
        User.user_list = []

    def test_user_save(self):
        """
        Test case to test if the user object is saved into the user_list.
        """
        self.new_user.user_save()
    
        self.assertEqual(len(User.user_list),1)

     def test_save_multiple_user(self):
        """
        Test to check whether we can save multiple user objects.
        """
        self.new_user.user_save()
        test_user = User("karimi","716491250","karimi@gmail.com")
        test_user.user_save()
        self.assertEqual(len(User.user_list),2) 

          def test_display_users(self):
        self.assertEqual(User.display_users(),User.user_list)

class TestCredentials(unittest.TestCase):
    """
    Test that define test cases for credentials.
    """
    def setUp(self):
        """ 
        set up method to run before each test cases
        """
        self.new_credential = Credentials("facebook","jonny govish", "jon88")

    def test_init(self):
        """
        Test case to test if the object is initialized properly.
        """

        self.assertEqual(self.new_credential.account_name,"facebook")
        self.assertEqual(self.new_credential.account_username,"jonny govish")
        self.assertEqual(self.new_credential.account_password,"jon88")
    