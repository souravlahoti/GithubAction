import unittest

from app import app


class ControllerUserListTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        # self.payload = {'its': 'empty'}

    def test_get_all_user_response(self):
        response = self.client.get('/api/users')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 2)


if __name__ == "__main__":
    unittest.main()
