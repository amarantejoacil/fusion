import uuid
from django.db import models

from stdimage.models import StdImageField

#funcao que gera nome aleatorio, ideal para img e anexos onde tem mts
# e pode repetir o numero.
#django ja faz o tratamento
def get_file_path(_instante, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Base(models.Model):
    criado = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Modificado', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Servico(Base):
    ICONE_CHOICE = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuário'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )
    servico = models.CharField('Serviço', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=12, choices=ICONE_CHOICE)

    class Meta:
        verbose_name = 'Serviço' #nome de apresentacao
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.servico


class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo

class Equipe(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    imagem = StdImageField('Imagem', upload_to='equipe', variations={'thumb':{'width': 480, 'height': 480, 'crop':True}})
   # imagem = StdImageField('Imagem', upload_to='get_file_path', variations={'thumb':{'width': 480, 'height': 480, 'crop':True}})
   # passa get_file_path que sao os nomes aleatorio
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome

class Recurso(Base):
    titulo = models.CharField('Titulo', max_length=100)
    descricao = models.CharField('Descricao', max_length=100)
    ICONE_CHOICE = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-laptop-phone', 'Laptop'),
        ('lni-leaf', 'Folha'),
        ('lni-rocket', 'Foguete'),
    )
    icone = models.CharField('Icone', max_length=30, choices=ICONE_CHOICE)

    class Meta:
        verbose_name = 'Recurso'
        verbose_name_plural = 'Recursos'

    def __str__(self):
        return self.titulo
