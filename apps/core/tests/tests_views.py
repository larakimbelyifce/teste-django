from django.test import TestCase
from django.urls import reverse


class PessoaViewTestCase(TestCase):

    def test_status_code_200(self):
        response = self.client.get(reverse('pessoa_view'))
        self.assertEquals(response.status_code, 200)

    def test_template_usado(self):
        response = self.client.get(reverse('pessoa_view'))
        self.assertTemplateUsed(response, 'pessoa_view.html')
