from django.shortcuts import render
from core.forms.add_user import AddUsuarioForm
from core.models.usuario import Usuario

def add_user(request):
    if request.method == 'POST':
        form = AddUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html', {'status': 'sucesso'})
        else:
            print(form.errors) 
            return render(request, 'index.html', {'status': 'erro'})
    
    form = AddUsuarioForm()
    return render(request, 'index.html', {'form': form})



def edit_user(id_user, request):
    pass




def remove_user(id_user, request):
    pass