import unittest


from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
    def test_city_country(self):
        self.assertEqual(city_country("santiago", "chile"), "Santiago, Chile")

if __name__ == "__main__":
    unittest.main()
