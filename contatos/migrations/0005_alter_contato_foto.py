# Generated by Django 4.0.6 on 2022-07-26 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0004_contato_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='foto',
            field=models.ImageField(blank=True, upload_to='media/fotos/%Y/%m/'),
        ),
    ]