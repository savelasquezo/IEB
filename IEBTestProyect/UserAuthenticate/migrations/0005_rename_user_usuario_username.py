# Generated by Django 4.1.3 on 2022-12-12 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserAuthenticate', '0004_rename_iebusuarios_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='user',
            new_name='username',
        ),
    ]
