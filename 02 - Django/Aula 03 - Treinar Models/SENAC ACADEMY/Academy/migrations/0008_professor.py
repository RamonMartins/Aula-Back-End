# Generated by Django 4.2.4 on 2023-08-23 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academy', '0007_curso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]