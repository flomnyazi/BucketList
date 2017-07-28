import unittest
from ..Activities.activity import Activity


class TestActivity(unittest.TestCase):
    
    def test_instance_of_activity(self):
        activity = Activity("hike longonot", "mountain climbing")
        self.assertIsInstance(activity, Activity)


if __name__ == '__main__':
    unittest.main()
