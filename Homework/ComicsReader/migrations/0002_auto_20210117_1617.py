# Generated by Django 3.1.4 on 2021-01-17 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ComicsReader', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='label',
            field=models.CharField(max_length=255, verbose_name='Подпись'),
        ),
    ]