import unittest

def soma(a, b):
    return a + b

class TesteSoma(unittest.TestCase):
    def test_soma_positivos(self):
        self.assertEqual(soma(2, 3), 5)

if __name__ == "__main__":
    unittest.main()