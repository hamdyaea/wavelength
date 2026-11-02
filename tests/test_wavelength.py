# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
import unittest
from wavelength import wavelength_m

class WavelengthTests(unittest.TestCase):
    def test_known_frequency(self):
        self.assertAlmostEqual(wavelength_m(299.792458), 1.0, places=7)
    def test_amateur_radio(self):
        self.assertAlmostEqual(wavelength_m(145.8), 2.05619, places=4)
    def test_invalid(self):
        for value in (0, -1, float("nan"), float("inf")):
            with self.assertRaises(ValueError):
                wavelength_m(value)

if __name__ == "__main__":
    unittest.main()
