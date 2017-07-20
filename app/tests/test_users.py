import unittest
from app.users.users import User


class TestUsers(unittest.TestCase):
    def test_user(self, ):
        new_user = User('mary poppins', 'mpoppins@test.com', 'password')
        self.assertIsInstance(new_user, User)                

if __name__ == '__main__':
    unittest.main()
