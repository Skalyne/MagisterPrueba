# Generated by Django 3.1.3 on 2020-11-25 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesores',
            name='movil',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
