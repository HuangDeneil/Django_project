# Generated by Django 2.2 on 2020-08-16 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gene_info',
            name='seq_length',
        ),
        migrations.AlterField(
            model_name='gene_info',
            name='sequence',
            field=models.TextField(default='example\n>seq \nATCGATGC'),
        ),
    ]
