from django.db import models

class Contrato(models.Model):
    data_emissao = models.DateField()
    data_nascimento_tomador = models.DateField()
    valor_desembolsado = models.DecimalField(max_digits=10, decimal_places=2)
    cpf = models.CharField(max_length=11)
    pais = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)
    cidade = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    taxa = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Contrato {self.id}"

class Parcela(models.Model):
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE, related_name='parcelas')
    numero = models.IntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_vencimento = models.DateField()

    def __str__(self):
        return f"Parcela {self.numero} do Contrato {self.contrato.id}"
