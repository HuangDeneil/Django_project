# Generated by Django 3.1 on 2020-09-29 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_db_search_log_reference_summary'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reference_summary',
            options={'ordering': ('db_id',)},
        ),
        migrations.AlterField(
            model_name='reference_summary',
            name='Halos_id',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]