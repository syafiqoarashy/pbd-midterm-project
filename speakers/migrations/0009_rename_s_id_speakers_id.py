# Generated by Django 4.1 on 2022-11-02 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0008_alter_speakers_s_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='speakers',
            old_name='s_id',
            new_name='id',
        ),
    ]
