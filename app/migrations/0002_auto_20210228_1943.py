# Generated by Django 2.2.10 on 2021-02-28 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anggota',
            name='bapak',
        ),
        migrations.RemoveField(
            model_name='anggota',
            name='ibu',
        ),
        migrations.RemoveField(
            model_name='anggota',
            name='job_bapak',
        ),
        migrations.RemoveField(
            model_name='anggota',
            name='job_ibu',
        ),
        migrations.AlterField(
            model_name='anggota',
            name='alamat',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='anggota',
            name='nama',
            field=models.CharField(max_length=255),
        ),
    ]
