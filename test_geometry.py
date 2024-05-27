import unittest
from geometry import volume_sphere, volume_cube, volume_cylinder

class TestVolumeCalculations(unittest.TestCase):

    def test_volume_sphere(self):
        self.assertAlmostEqual(volume_sphere(1), 4.18879, places=5)
        self.assertAlmostEqual(volume_sphere(2), 33.51032, places=5)
        self.assertAlmostEqual(volume_sphere(0), 0, places=5)
        with self.assertRaises(ValueError):
            volume_sphere(-1)

    def test_volume_cube(self):
        self.assertAlmostEqual(volume_cube(1), 1)
        self.assertAlmostEqual(volume_cube(2), 8)
        self.assertAlmostEqual(volume_cube(0), 0)
        with self.assertRaises(ValueError):
            volume_cube(-1)

    def test_volume_cylinder(self):
        self.assertAlmostEqual(volume_cylinder(1, 1), 3.14159, places=5)
        self.assertAlmostEqual(volume_cylinder(2, 3), 37.69911, places=5)
        self.assertAlmostEqual(volume_cylinder(0, 1), 0, places=5)
        with self.assertRaises(ValueError):
            volume_cylinder(-1, 1)
        with self.assertRaises(ValueError):
            volume_cylinder(1, -1)

if __name__ == '__main__':
    unittest.main()