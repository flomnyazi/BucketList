import unittest
from app.users.users import User


class TestUser(unittest.TestCase):
    def test_is_type(self):
        new_user = User('mary poppins', 'mpoppins@test.com', 'password')
        self.assertIsInstance(new_user, User)


if __name__ == '__main__':
    unittest.main()
