# Generated by Django 4.1 on 2022-10-29 22:24

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventsgeneral',
            name='time',
        ),
        migrations.AddField(
            model_name='eventsgeneral',
            name='endTime',
            field=models.CharField(default=django.utils.timezone.now, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eventsgeneral',
            name='startTime',
            field=models.CharField(default=django.utils.timezone.now, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='eventsgeneral',
            name='speaker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='events.speakers'),
        ),
    ]
