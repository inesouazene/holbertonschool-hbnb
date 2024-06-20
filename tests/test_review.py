import unittest
from models.review import Review
from models.user import User
from models.place import Place

class TestReview(unittest.TestCase):
    def setUp(self):
        User.clear_users()

    def test_review_creation(self):
        user = User(email="reviewer@example.com", password="securepassword")
        host = User(email="host@example.com", password="securepassword")
        place = Place(name="Test Place", description="A place for testing", address="123 Test St", city="Test City", latitude=0.0, longitude=0.0, host=host, number_of_rooms=2, number_of_bathrooms=1, price_per_night=100, max_guests=4)
        review = Review(user=user, place=place, content="Great place!", rating=5)
        self.assertIsNotNone(review.id)
        self.assertEqual(review.user, user)
        self.assertEqual(review.place, place)
        self.assertEqual(review.content, "Great place!")
        self.assertEqual(review.rating, 5)

if __name__ == '__main__':
    unittest.main()
