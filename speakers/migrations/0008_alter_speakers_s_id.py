# Generated by Django 4.1 on 2022-11-02 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0007_rename_id_speakers_s_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speakers',
            name='s_id',
            field=models.CharField(max_length=15, primary_key=True, serialize=False),
        ),
    ]
