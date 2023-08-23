# Generated by Django 4.2.4 on 2023-08-23 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alunos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome do Aluno')),
                ('idade', models.IntegerField()),
                ('data_de_nascimento', models.DateField()),
                ('status', models.TextField()),
                ('peso', models.DecimalField(decimal_places=2, max_digits=3)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1)),
                ('sobre_mim', models.TextField()),
            ],
        ),
    ]