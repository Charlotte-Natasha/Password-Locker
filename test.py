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