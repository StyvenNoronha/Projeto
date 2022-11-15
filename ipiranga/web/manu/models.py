from django.db import models
from funcionarios.models import funcionario
# Create your models here.


class Motor(models.Model):
    modelo=models.CharField(max_length=10,null=False, blank=False)
    voltagem=models.IntegerField(null=False, blank=False)
    corrente=models.IntegerField(null=False, blank=False)
    CV=models.IntegerField(null=False, blank=False)
    RPM=models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.modelo
    #devolver o modelo do motor


class Manutencao(models.Model):
    fk_codEletrista = models.OneToOneField(funcionario, on_delete=models.DO_NOTHING)
    fk_codMotor = models.ForeignKey(Motor, on_delete=models.DO_NOTHING)
    data = models.DateField(null=False, blank=False)
    hora = models.TimeField(null=False, blank=False)
    desc_Pro = models.TextField(max_length=1000, null=False, blank=False)
    desc_Solu = models.TextField(max_length=1000, null=False, blank=False)
    valor_servico = models.FloatField(null=False, blank=False)

    def __str__(self):
        return self.desc_Pro
    # devolver data