# Generated by Django 2.1.4 on 2019-03-02 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('acak_kata_apps', '0002_delete_kata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kata', models.CharField(max_length=256, unique=True)),
            ],
        ),
    ]
