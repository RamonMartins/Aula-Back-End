# Generated by Django 4.2.4 on 2023-09-08 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('criadores', '0001_initial'),
        ('tarefas', '0004_remove_tarefa_responsavel_tarefa_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarefa',
            name='responsavel_tarefa',
        ),
        migrations.AddField(
            model_name='tarefa',
            name='responsavel_tarefa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='criadores.criador'),
        ),
    ]