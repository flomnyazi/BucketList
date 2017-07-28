import unittest
from ..bucketlists.bucketlists import BucketList
from ..Activities.activity import Activity


class TestBucketList(unittest.TestCase):
    
    def test_instance_if_bucketlist(self):
        bucket1 = BucketList('bname', 1)
        self.assertIsInstance(bucket1, BucketList)
    
if __name__ == '__main__':
    unittest.main( )
