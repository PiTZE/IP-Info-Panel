# Generated by Django 4.2.6 on 2023-10-31 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IIP', '0003_server_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
