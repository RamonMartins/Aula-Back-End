# Generated by Django 4.2.4 on 2023-08-21 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='ano_lancamento',
            field=models.IntegerField(max_length=4),
        ),
    ]