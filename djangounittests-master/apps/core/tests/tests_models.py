from django.test import TestCase

from ..models import Pessoa

# Create your tests here.


class PessoaTestCase(TestCase):

    def setUp(self):
        Pessoa.objects.create(
            nome="Francisco André",
            idade=38
        )

    def test_retorno_str(self):
        p1 = Pessoa.objects.get(nome='Francisco André')
        self.assertEquals(p1.__str__(), 'Francisco André')
