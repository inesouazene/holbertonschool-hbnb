import unittest
from models.place import Place
from models.user import User

class TestPlace(unittest.TestCase):
    def setUp(self):
        User.clear_users()

    def test_place_creation(self):
        host = User(email="host@example.com", password="securepassword")
        place = Place(name="Test Place", description="A place for testing", address="123 Test St", city="Test City", latitude=0.0, longitude=0.0, host=host, number_of_rooms=2, number_of_bathrooms=1, price_per_night=100, max_guests=4)
        self.assertIsNotNone(place.id)
        self.assertEqual(place.name, "Test Place")
        self.assertEqual(place.host, host)

    def test_add_amenity(self):
        host = User(email="host@example.com", password="securepassword")
        place = Place(name="Test Place", description="A place for testing", address="123 Test St", city="Test City", latitude=0.0, longitude=0.0, host=host, number_of_rooms=2, number_of_bathrooms=1, price_per_night=100, max_guests=4)
        amenity = "WiFi"
        place.add_amenity(amenity)
        self.assertIn(amenity, place.amenities)

if __name__ == '__main__':
    unittest.main()
