# Generated by Django 3.2.6 on 2021-08-29 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0003_filesmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filesmodel',
            old_name='filename',
            new_name='uploaded_file',
        ),
    ]
