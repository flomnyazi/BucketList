import unittest
from app import app


class TestApp(unittest.TestCase):
    def test_urls(self):
        client = app.test_client(self)
        result = client.get('/')
        self.assertEqual(result.status_code, 200)


if __name__ == '__main__':
    unittest.main()