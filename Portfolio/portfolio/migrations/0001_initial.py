# Generated by Django 5.0.7 on 2024-07-24 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='projets/')),
                ('url', models.URLField(blank=True)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
