import unittest
from app.bucketlists.bucketlists import BucketList
from app.items.items import Item


class TestBucketList(unittest.TestCase):
    def test_is_type(self):
        new_bucketlist = BucketList('BucketList 1')
        self.assertIsInstance(new_bucketlist, BucketList)


if __name__ == '__main__':
    unittest.main()
