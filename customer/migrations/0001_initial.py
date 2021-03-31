# Generated by Django 3.1.7 on 2021-03-31 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerName', models.CharField(max_length=20)),
                ('customerEmail', models.EmailField(max_length=50)),
                ('customerContact', models.CharField(max_length=11)),
                ('customerPassword', models.CharField(max_length=20)),
            ],
        ),
    ]