import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        User.clear_users()

    def test_user_creation(self):
        user = User(email="test@example.com", password="securepassword")
        self.assertIsNotNone(user.id)
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")
        self.assertIsNotNone(user.created_at)
        self.assertIsNotNone(user.updated_at)

    def test_unique_email(self):
        user1 = User(email="test@example.com", password="securepassword")
        with self.assertRaises(ValueError):
            User(email="test@example.com", password="anotherpassword")

if __name__ == '__main__':
    unittest.main()
