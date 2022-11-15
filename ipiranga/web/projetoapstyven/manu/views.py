from django.shortcuts import render
from .models import Motor,Manutencao
from funcionarios.models import Funcao,funcionario
from django.utils.html import format_html
# Create your views here.

def cadmotor(request):
    if request.method == 'POST':
        modelo = request.POST['modelo']
        voltagem = request.POST['voltagem']
        corrente = request.POST['corrente']
        CV = request.POST['CV']
        RPM = request.POST['RPM']

        resultado = Motor.objects.create(modelo=modelo,voltagem=voltagem,corrente=corrente,CV=CV,RPM=RPM)
        resultado.save()



        return render(request, 'manutencao/CadMotor.html')
    else:
     return render(request, 'manutencao/CadMotor.html')


def manutencao(request):
    nome = funcionario.objects.all()
    modelo = Motor.objects.all()

    if request.method == 'POST':

     fk_codEletrista = funcionario.objects.get(id=int(request.POST['fk_codEletrista']))
     fk_codMotor = Motor.objects.get(id=int(request.POST['fk_codMotor']))
     data = request.POST['data']
     hora = request.POST['hora']
     desc_Pro = request.POST['desc_Pro']
     desc_Solu = request.POST['desc_Solu']
     valor_servico = request.POST['valor_servico']
     resul= Manutencao.objects.create(fk_codEletrista=fk_codEletrista,fk_codMotor=fk_codMotor,data=data,hora=hora,desc_Pro=desc_Pro,desc_Solu=desc_Solu,valor_servico=valor_servico)
     resul.save()

     return render(request, 'manutencao/cadManu.html',{'modelo':modelo,'nome':nome})
    else:
     return render(request, 'manutencao/cadManu.html',{'modelo':modelo,'nome':nome})