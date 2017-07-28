import unittest
from app.app import *
from ..bucketlists.bucketlists import BucketList
from ..users.users import User


class TestApp(unittest.TestCase):
    
    def setUp(self):
        self.user1 = User("Name 1", "user@email.com", "username1", "username1")
        self.user1.id = 1
    
    def test_a_user_can_sign_up(self):
        response = self.client.post('/signup', self.user1)
        self.assertEqual(response.status_code, 200)

    def test_a_user_can_login(self):
        response = self.client.post('/login', self.user1)
        self.assertEqual(response.status_code, 200)
        

    def test_a_user_can_logout(self):
        response = self.client.post('/logout', self.user1)
        self.assertEqual(response.status_code, 200)
        
    def test_can_create_a_bucketlist(self):
        self.buckets.Bucketlists = {}
        output = self.buckets.create('Bucketlist 1', 'Fashion','owner@gmail.com')
        self.assertEqual(1,output, "Bucket successfully created")
    

    def test_can_list_bucketlists(self):
        response = self.client.post('/mybucketlist', self.user1)
        self.assertEqual(response.status_code, 200)

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
    

