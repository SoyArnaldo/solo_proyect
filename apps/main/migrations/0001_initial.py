# Generated by Django 4.2.6 on 2023-10-22 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conocimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conocimiento', models.TextField()),
                ('public', models.DateTimeField(auto_now_add=True, verbose_name='Publicado')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado')),
                ('link_video', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'Conocimientos',
                'db_table': 'conocimiento',
                'ordering': ['-public'],
            },
        ),
    ]
