from django.contrib import admin

# Register your models here.

from .models import Cargo, Servico, Equipe, Recurso

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display =('cargo', 'ativo', 'modificado')

@admin.register(Servico)
class CargoAdmin(admin.ModelAdmin):
    list_display =('servico', 'icone', 'ativo', 'modificado')

@admin.register(Equipe)
class CargoAdmin(admin.ModelAdmin):
    list_display =('nome', 'cargo', 'ativo', 'modificado')

@admin.register(Recurso)
class Recurso(admin.ModelAdmin):
    list_display = ('titulo', 'descricao',  'modificado')
