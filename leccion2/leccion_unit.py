import unittest
import operaciones


class PruebasUnitarias(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(operaciones.suma(18, 2), 20)
    def test_resta(self):
        self.assertEqual(operaciones.resta(10, 5), 5)


if __name__ == '__main__':
    unittest.main()
