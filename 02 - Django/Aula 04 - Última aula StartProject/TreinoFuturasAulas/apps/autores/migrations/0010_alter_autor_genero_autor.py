# Generated by Django 4.2.4 on 2023-08-25 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0002_genero'),
        ('autores', '0009_autor_genero_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='genero_autor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='livros.genero'),
        ),
    ]
