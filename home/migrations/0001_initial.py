# Generated by Django 4.1 on 2022-11-02 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='Guest', max_length=255)),
                ('content', models.TextField()),
                ('institute', models.CharField(max_length=255)),
            ],
        ),
    ]