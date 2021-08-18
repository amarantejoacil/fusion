# Generated by Django 3.2.6 on 2021-08-18 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Modificado')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descricao')),
                ('icone', models.CharField(choices=[('lni-cog', 'Engrenagem'), ('lni-stats-up', 'Gráfico'), ('lni-laptop-phone', 'Laptop'), ('lni-leaf', 'Folha'), ('lni-rocket', 'Foguete')], max_length=30, verbose_name='Icone')),
            ],
            options={
                'verbose_name': 'Recurso',
                'verbose_name_plural': 'Recursos',
            },
        ),
        migrations.AlterField(
            model_name='equipe',
            name='instagram',
            field=models.CharField(default='#', max_length=100, verbose_name='Instagram'),
        ),
        migrations.AlterField(
            model_name='equipe',
            name='twitter',
            field=models.CharField(default='#', max_length=100, verbose_name='Twitter'),
        ),
    ]
