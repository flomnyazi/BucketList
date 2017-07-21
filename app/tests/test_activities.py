import unittest
from app.Activities.activity import Activity


class TestActivity(unittest.TestCase):
    
    def test_an_instance_of_activity(self):
        self.assertIsInstance(self.activity, Activity)


if __name__ == '__main__':
    unittest.main()
