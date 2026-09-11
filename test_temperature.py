import unittest

from temperature import (
    celsius_to_fahrenheit,
    celsius_to_kelvin,
    fahrenheit_to_celsius,
    kelvin_to_celsius,
)


class CelsiusToFahrenheitTests(unittest.TestCase):
    def test_freezing_point(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32)

    def test_boiling_point(self):
        self.assertEqual(celsius_to_fahrenheit(100), 212)


class FahrenheitToCelsiusTests(unittest.TestCase):
    def test_freezing_point(self):
        self.assertEqual(fahrenheit_to_celsius(32), 0)

    def test_boiling_point(self):
        self.assertEqual(fahrenheit_to_celsius(212), 100)


class CelsiusToKelvinTests(unittest.TestCase):
    def test_absolute_zero(self):
        self.assertAlmostEqual(celsius_to_kelvin(-273.15), 0)

    def test_freezing_point(self):
        self.assertAlmostEqual(celsius_to_kelvin(0), 273.15)


class KelvinToCelsiusTests(unittest.TestCase):
    def test_absolute_zero(self):
        self.assertAlmostEqual(kelvin_to_celsius(0), -273.15)

    def test_freezing_point(self):
        self.assertAlmostEqual(kelvin_to_celsius(273.15), 0)


if __name__ == "__main__":
    unittest.main()