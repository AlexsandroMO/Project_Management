# Generated by Django 4.0.1 on 2022-01-18 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentlistproject',
            name='name_doc',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='NOME DO DOCUMENTO'),
        ),
    ]
