from django.db import models

class Funcao(models.Model):

    descricao = models.CharField(max_length=50, null=False, blank=False)
    valor_horac = models.FloatField(null=False, blank=False)

    def __str__(self):
        return self.descricao

class funcionario(models.Model):
    nome = models.CharField(max_length=60, null=False, blank=False)
    RG = models.CharField(max_length=12, null=False, blank=False)
    CPF = models.CharField(max_length=14, null=False, blank=False)
    funcao=models.ForeignKey(Funcao, on_delete=models.DO_NOTHING )
    celular = models.CharField(max_length=14, null=True, blank=True)
    rua = models.CharField(max_length=100, null=False, blank=False)
    numeroCasa = models.IntegerField(null=False, blank=False)
    bairro = models.CharField(max_length=100, null=False, blank=False)
    cidade = models.CharField(max_length=100, null=False, blank=False)
    estado = models.CharField(max_length=2, null=False, blank=False)
    CEP = models.CharField(max_length=10, null=False, blank=False)

    def __str__(self):
        return self.nome

        # devolver o nome do  funcionario


