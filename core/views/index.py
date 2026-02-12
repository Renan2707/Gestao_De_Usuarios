from django.shortcuts import render
from core.models.usuario import Usuario

def index(request):
    usuarios = Usuario.objects.all()
    usuarios_ativos = usuarios.filter(status=True).count()
    usuarios_inativos = usuarios.filter(status=False).count()
    return render(request, 'index.html', {'usuarios': usuarios, 'usuarios_ativos': usuarios_ativos, 'usuarios_inativos': usuarios_inativos})