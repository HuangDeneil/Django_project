# Generated by Django 3.1 on 2020-08-19 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_auto_20200817_0650'),
    ]

    operations = [
        migrations.CreateModel(
            name='reference_summary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db_id', models.TextField(default='暫無說明', null=True)),
                ('orgranism_name', models.TextField(default='暫無說明', null=True)),
                ('chinese_name', models.TextField(default='暫無說明', null=True)),
                ('genus', models.TextField(default='unkown genus', null=True)),
                ('species_name', models.TextField(default='unkown species', null=True)),
                ('gram_stain', models.TextField(default='', null=True)),
                ('top_type', models.TextField(default='', null=True)),
                ('source', models.TextField(default='', null=True)),
                ('key_word', models.TextField(default='暫無說明', null=True)),
                ('Halos_id', models.TextField(default='暫無說明', null=True)),
                ('taxid', models.TextField(default='暫無說明', null=True)),
                ('Description', models.TextField(default='no description', null=True)),
                ('reference1', models.TextField(default='no reference', null=True)),
                ('reference2', models.TextField(null=True)),
                ('reference3', models.TextField(null=True)),
                ('reference4', models.TextField(null=True)),
                ('reference5', models.TextField(null=True)),
                ('date', models.DateField(auto_now=True, null=True)),
                ('data_source', models.TextField(default='unknow', null=True)),
                ('data_status', models.TextField(default='unknow', null=True)),
            ],
        ),
    ]