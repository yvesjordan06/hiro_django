# Generated by Django 2.2.7 on 2019-11-22 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('btpp', '0003_auto_20191122_1916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tache',
            name='metier',
        ),
        migrations.AddField(
            model_name='metier',
            name='taches',
            field=models.ManyToManyField(to='btpp.Tache'),
        ),
    ]