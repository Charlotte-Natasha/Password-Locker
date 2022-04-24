import unittest
from main import User
from main import Credentials


class UserTest(unittest.TestCase):
    """
    Define testcase for credentials class behaviour.

    unittest.testcase: helps in creating test cases
    """

    def setUp(self):
        """
        Runs before each test case
        :return:
        """
        self.new_user = Credentials("Instagram", "Charlotte", "#123")

    def test_init(self):
        """
        Checks if the function is initialized properly
        :return:
        """
        self.assertEqual(self.new_user.account, "Instagram")
        self.assertEqual(self.new_user.username, "Charlotte")
        self.assertEqual(self.new_user.password, "#123")

    def test_save_credentials(self):
        """
        Test case to test if credential objects are saved
        :return:
        """
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_details), 1)

    def tearDown(self) :
        """
        Cleans up after each test case has run
        :return:
        """
        Credentials.credentials_details = []

    def test_save_multiple_credentials(self):
        """
        checks if we can save multiple credentials
        :return:
        """
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Account", "User", "Password")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_details), 2)

    def test_delete_credentials(self):
        """
        To test if we can remove a credential from our credential list
        :return:
        """
        self.new_user.save_credentials()
        test_credentials = Credentials("Account", "User", "Password")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_details))