# Generated by Django 3.2 on 2022-04-21 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0013_auto_20220421_0322'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_number', models.IntegerField(null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('zipcode', models.IntegerField(null=True)),
                ('landmark2', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='tickets',
            name='document',
        ),
    ]
