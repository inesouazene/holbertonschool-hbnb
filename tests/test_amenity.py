import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def test_amenity_creation(self):
        amenity = Amenity(name="WiFi")
        self.assertIsNotNone(amenity.id)
        self.assertEqual(amenity.name, "WiFi")
        self.assertIsNotNone(amenity.created_at)
        self.assertIsNotNone(amenity.updated_at)

if __name__ == '__main__':
    unittest.main()
