# Generated by Django 2.0 on 2017-12-07 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mascota',
            name='id',
        ),
        migrations.AddField(
            model_name='mascota',
            name='folio',
            field=models.CharField(default=3, max_length=10, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
