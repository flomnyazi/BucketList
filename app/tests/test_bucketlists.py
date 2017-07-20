import unittest
from app.bucketlists.bucketlists import BucketList
from app.items.items import Item


class TestBucketList(unittest.TestCase):
    def setUp(self):
        self.bucketlist = Bucketlist()

    def test_create_bucketlist(self):
        output = self.bucketlist.create('BucketList 1', 'my goals')
        self.assertEqual(1, output, "BucketList successfully created")

    def test_edit_bucketlist(self):
        output = self.bucketlist.edit('BucketList 1', 'my new goals')
        self.assertEqual(1, output, "BucketList successfully edited")

    def test_delete_bucketlist(self):
        output = self.bucketlist.delete("BucketList 1", "my goals")
        self.assertEqual(1, output, "BucketList successfully deleted")


if __name__ == '__main__':
    unittest.main()
