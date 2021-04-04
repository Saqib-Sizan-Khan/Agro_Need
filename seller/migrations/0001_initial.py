# Generated by Django 3.1.7 on 2021-04-04 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sellerName', models.CharField(max_length=20)),
                ('sellerEmail', models.EmailField(max_length=50)),
                ('sellerContact', models.CharField(max_length=11)),
                ('sellerPassword', models.CharField(max_length=20)),
                ('rating', models.IntegerField()),
            ],
            options={
                'db_table': 'Seller Info',
            },
        ),
        migrations.CreateModel(
            name='TemporaryS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sellerName', models.CharField(max_length=20)),
                ('sellerPassword', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Seller Temporary Data',
            },
        ),
    ]
