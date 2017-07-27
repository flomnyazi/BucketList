import unittest
from app import app
from bucketlists.bucketlists import BucketList
from users.users import User


class TestApp(unittest.TestCase):
    
    def setUp(self):
        self.user1 = User()
        self.user1.name = "Name 1"
        self.user1.email = "user@email.com"
        self.user1.userName = "username1"
        self.user1.password = "passWd"
        self.user1.id = 1
    
    def test_a_user_can_sign_up(self):
        pass

    def test_a_user_can_login(self):
        pass

    def test_a_user_can_logout(self):
        pass

    def testit_can_create_a_bucketlist(self):
        pass

    def test_can_list_bucketlists(self):
        pass

    def test_can_update_a_bucketlist(self):
        self

    def test_can_delete_a_bucket_list(self):
        pass

    def test_can_create_activity(self):
        pass

    def test_can_edit_activity(self):
        pass

    def test_can_delete_activity(self):
        pass


if __name__ == '__mian__':
    unittest.main
    

if __name__ == '__main__':
    unittest.main()