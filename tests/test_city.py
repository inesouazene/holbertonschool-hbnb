import unittest
from models.city import City
from models.country import Country
from models.place import Place
from models.user import User

class TestCity(unittest.TestCase):
    def test_city_creation(self):
        country = Country(name="Test Country")
        city = City(name="Test City", country=country)
        self.assertIsNotNone(city.id)
        self.assertEqual(city.name, "Test City")
        self.assertEqual(city.country, country)
        self.assertIsNotNone(city.created_at)
        self.assertIsNotNone(city.updated_at)

    def test_add_place(self):
        country = Country(name="Test Country")
        city = City(name="Test City", country=country)
        host = User(email="host@example.com", password="securepassword")
        place = Place(name="Test Place", description="A place for testing", address="123 Test St", city=city, latitude=0.0, longitude=0.0, host=host, number_of_rooms=2, number_of_bathrooms=1, price_per_night=100, max_guests=4)
        city.add_place(place)
        self.assertIn(place, city.places)

if __name__ == '__main__':
    unittest.main()
