import unittest

class Calculadora:
    def somar(self, a, b):
        return a + b
    def dividir(self, a, b):
        return a / b

class TesteCalculadora(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_somar(self):
        self.assertEqual(self.calc.somar(4, 2), 6)

    def test_dividir(self):
        self.assertEqual(self.calc.dividir(10, 2), 5)

if __name__ == "__main__":
    unittest.main()