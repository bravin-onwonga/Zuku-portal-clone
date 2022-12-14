# Generated by Django 3.2 on 2022-04-20 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0010_auto_20220421_0127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shiftingrequest',
            name='client',
        ),
        migrations.AddField(
            model_name='packages',
            name='email',
            field=models.EmailField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='shiftingrequest',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='packages',
            name='package_type',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
