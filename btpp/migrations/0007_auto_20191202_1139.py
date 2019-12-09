# Generated by Django 2.2.7 on 2019-12-02 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('btpp', '0006_annonce_lieu'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='annonce',
            name='taxation',
        ),
        migrations.CreateModel(
            name='Abonnement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intitule', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=20)),
                ('prix', models.CharField(max_length=20)),
                ('taches', models.ManyToManyField(to='btpp.Tache')),
            ],
        ),
    ]
