# Generated by Django 3.2 on 2022-04-20 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0009_auto_20220420_2217'),
    ]

    operations = [
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.IntegerField(null=True)),
                ('package_type', models.CharField(choices=[('basic', 'Triple Pay 10 Mbps'), ('classic', 'Triple Pay 20 Mbps'), ('platinum', 'Triple Pay 30Mbps')], default='BASIC', max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Refer',
        ),
    ]
