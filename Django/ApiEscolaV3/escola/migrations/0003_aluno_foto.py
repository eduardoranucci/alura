# Generated by Django 4.1 on 2022-08-24 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0002_aluno_celular'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='foto',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
