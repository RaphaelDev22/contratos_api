from django.test import TestCase
from .models import Contrato, Parcela

class ContratoTestCase(TestCase):
    def setUp(self):
        contrato = Contrato.objects.create(
            data_emissao="2023-06-01",
            data_nascimento_tomador="1990-01-01",
            valor_desembolsado=10000,
            cpf="12345678901",
            pais="Brasil",
            estado="SP",
            cidade="São Paulo",
            telefone="11999999999",
            taxa=2.5
        )
        Parcela.objects.create(contrato=contrato, numero=1, valor=5000, data_vencimento="2023-07-01")
        Parcela.objects.create(contrato=contrato, numero=2, valor=5000, data_vencimento="2023-08-01")

    def test_contrato_created(self):
        contrato = Contrato.objects.get(cpf="12345678901")
        self.assertEqual(contrato.valor_desembolsado, 10000)
        self.assertEqual(contrato.parcelas.count(), 2)
