# Generated by Django 4.0.6 on 2022-07-20 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_produtos_color_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produtos',
            name='color_code',
        ),
    ]