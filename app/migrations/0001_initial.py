# Generated by Django 2.2.10 on 2021-02-28 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Devisi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('devisi', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Anggota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nim', models.IntegerField()),
                ('nama', models.CharField(max_length=255, verbose_name='Nama')),
                ('alamat', models.TextField(verbose_name='Alamat Lengkap')),
                ('tempat_lahir', models.CharField(max_length=255)),
                ('tanggal_lahir', models.DateField()),
                ('jenis_kelamin', models.CharField(max_length=255)),
                ('prodi', models.CharField(max_length=255)),
                ('semester', models.IntegerField()),
                ('keterangan', models.TextField()),
                ('bapak', models.CharField(max_length=255)),
                ('ibu', models.CharField(max_length=255)),
                ('job_bapak', models.CharField(max_length=255)),
                ('job_ibu', models.CharField(max_length=255)),
                ('nomor_hp', models.BigIntegerField()),
                ('facebook', models.CharField(max_length=255)),
                ('devisi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Devisi')),
            ],
        ),
    ]
