import unittest
from models.country import Country
from models.city import City

class TestCountry(unittest.TestCase):
    def test_country_creation(self):
        country = Country(name="Test Country")
        self.assertIsNotNone(country.id)
        self.assertEqual(country.name, "Test Country")
        self.assertIsNotNone(country.created_at)
        self.assertIsNotNone(country.updated_at)

    def test_add_city(self):
        country = Country(name="Test Country")
        city = City(name="Test City", country=country)
        country.add_city(city)
        self.assertIn(city, country.cities)

if __name__ == '__main__':
    unittest.main()
