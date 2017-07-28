import unittest
from ..users.users import User


class TestUser(unittest.TestCase):
    
    def test_instance_of_user(self):
        user = User("Flo", "flo@mail.co", "flo", "pass")
        self.assertIsInstance(user, User)


if __name__ == '__main__':
    unittest.main()
