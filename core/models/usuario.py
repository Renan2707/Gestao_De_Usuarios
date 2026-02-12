from core.models.base import BaseModel
from django.db import models

class Usuario(BaseModel):
    nome = models.CharField(max_length=150)
    cargo = models.CharField(max_length=150)
    status = models.BooleanField('Usuário Ativo?',default=True,)
    
    class Meta:
            ordering = ('nome',)
            verbose_name = 'Usuário'
            verbose_name_plural = 'Usuários'
            
    def __str__(self):
        return f'{self.nome} - {self.status}'