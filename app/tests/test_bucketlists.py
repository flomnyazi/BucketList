`import unittest
from app.bucketlists.bucketlists import BucketList
from app.activity.activity import Activity
from app.app import bucketlists as my_bucketlists


class TestBucketList(unittest.TestCase):
    
    def test_an_instance_of_bucketlist(self):
        self.assertIsInstance(self.bucketlist, BucketList)


if __name__ == '__main__':
    unittest.main( )
