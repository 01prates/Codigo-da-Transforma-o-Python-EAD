import unittest

class Calculadora:
    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Divisão por zero não permitida")
        return a / b

class TesteExcecao(unittest.TestCase):
    def test_divisao_por_zero(self):
        calc = Calculadora()
        with self.assertRaises(ValueError):
            calc.dividir(5, 0)

if __name__ == "__main__":
    unittest.main()