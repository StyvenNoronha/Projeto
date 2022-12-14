from django.shortcuts import render, get_object_or_404, redirect
from .models import funcionario,Funcao
from django.utils.html import format_html
   #import para pdf
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from django.http import HttpResponse

# Create your views here.



def cad(request):
    funcao = Funcao.objects.all()
    if request.method =='POST':
            func = Funcao.objects.get(pk=int(request.POST['funcao']))
            nome = request.POST['nome']
            RG = request.POST['RG']
            CPF = request.POST['CPF']
            celular = request.POST['celular']
            rua = request.POST['rua']
            numeroCasa = request.POST['numeroCasa']
            bairro = request.POST['bairro']
            estado = request.POST['estado']
            CEP = request.POST['CEP']
            cidade=request.POST['cidade']

            funcionarios = funcionario.objects.create(nome=nome,RG=RG,CPF=CPF,celular=celular,rua=rua,numeroCasa=numeroCasa,bairro=bairro,estado=estado,CEP=CEP,cidade=cidade,
                                                      funcao=func)
            msg = format_html('<div class="alert alert-success alert-dismissible"> '
                              'Cadastro de funcionarios'
                              '<br>'
                              ' Realizado com sucesso '
                              '</div>')
            funcionarios.save()

            return render(request, 'funcionarios/cadFun.html',{'mensagem':msg,'funcao':funcao})
    else:



        return render(request, 'funcionarios/cadFun.html',{'funcao':funcao})


def lista(request,pk=None):
    funcionarios = funcionario.objects.all()
    if request.method =='GET':
        if pk!=None:
         apagar = funcionario.objects.get(pk=pk)
         msg = format_html('<div class="alert alert-danger" role="alert"> '
                           'Promovido a cliente'
                           '<br>'
                           ' Desligado da empresa'
                           '</div>')
         apagar.delete()
         return render(request, 'funcionarios/listFun.html', {'name': funcionarios,'mensagem':msg})
        else:
            funcionarios = funcionario.objects.all()
            return render(request, 'funcionarios/listFun.html',{'name':funcionarios})
    else:
            return render(request, 'funcionarios/listFun.html', {'name': funcionarios})


def cargo(request):

    if request.method == 'POST':

          descricao=request.POST['descricao']
          valor_horac=request.POST['valor_horac']
          resultado= Funcao.objects.create(descricao=descricao,valor_horac=valor_horac)
          resultado.save()
          msg = format_html('<div class="alert alert-success alert-dismissible"> '
                            'Cadastro de cargo'
                            '<br>'
                            ' Realizado com sucesso '
                            '</div>')
          return render(request, 'funcionarios/cad_cargo.html',{'mensagem':msg})

    else:

        return render(request, 'funcionarios/cad_cargo.html')

def listapdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    funcionarios = funcionario.objects.all()
    lines = []
    for funci in funcionarios:
        lines.append(funci.nome)
        lines.append(funci.celular)
        lines.append('*************')

    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename='Lista de funcionario.pdf')

