# Generated by Django 2.2.10 on 2021-03-29 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210318_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='JadwalDiskusi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hari', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('devisi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Devisi')),
            ],
        ),
    ]
