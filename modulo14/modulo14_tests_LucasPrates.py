from django.test import TestCase
from .models import Produto

class ProdutoTestCase(TestCase):
    def setUp(self):
        Produto.objects.create(nome="Mouse", descricao="Sem fio", preco=50.0, quantidade=20)

    def test_criacao_produto(self):
        p = Produto.objects.get(nome="Mouse")
        self.assertEqual(p.quantidade, 20)