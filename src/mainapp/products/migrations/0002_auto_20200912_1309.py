# Generated by Django 3.1.1 on 2020-09-12 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='type',
            field=models.CharField(choices=[('appetizers', 'appetizers'), ('entrees', 'entrees'), ('deserts', 'deserts'), ('drinks', 'drinks')], max_length=60),
        ),
    ]
