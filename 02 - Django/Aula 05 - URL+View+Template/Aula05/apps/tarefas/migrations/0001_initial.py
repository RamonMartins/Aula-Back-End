# Generated by Django 4.2.4 on 2023-08-29 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao_tarefa', models.CharField(max_length=200)),
                ('concluida', models.BooleanField(default=False)),
            ],
        ),
    ]
