from django.test import TestCase
from django.urls import reverse

from .models import Usuario


class UsuarioViewsTests(TestCase):
    def test_adicionar_usuario_post(self):
        response = self.client.post(
            reverse('adicionar_usuario'),
            {
                'nome': 'Ana',
                'email': 'ana@email.com',
                'senha': '123456',
                'cpf': '12345678901',
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(Usuario.objects.filter(email='ana@email.com').exists())
