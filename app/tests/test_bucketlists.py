import unittest
from app.bucketlists.bucketlists import BucketList
from app.items.items import Item


class TestBucketLists(unittest.TestCase):
    def BucketList(self):
        self.bucket_list = BucketList('BucketList 1',)

    def test_create_activity(self):
        new_activity = self.bucket_list.create_activity('Learn to Scuba dive')
        self.assertIsInstance(new_activity, Activity)

    def test_view_activity(self):
        pass

    def test_edit_activity(self):
        pass
