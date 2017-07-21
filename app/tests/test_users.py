import unittest
from app.users.users import User


class TestUser(unittest.TestCase):
    
    def test_an_instance_of_user(self):
        self.assertIsInstance(self.user, User)


if __name__ == '__main__':
    unittest.main()
