import unittest

from conversoes import converte_para_celsius, converte_para_fahrenheit

class TestConversoes(unittest.TestCase):
    def test_converte_para_fahrenheit(self):
        self.assertAlmostEqual(converte_para_fahrenheit(0), 32.0, places=1)
        self.assertAlmostEqual(converte_para_fahrenheit(27), 80.6, places=1)

    def test_converte_para_celsius(self):
        self.assertAlmostEqual(converte_para_celsius(32), 0, places=1)
        self.assertAlmostEqual(converte_para_celsius(41), 5.0, places=1)

if __name__ == '__main__':
    unittest.main()