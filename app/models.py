# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

# Create your models here.

class Devisi(models.Model):
    devisi = models.CharField(max_length=255)
    
    def __str__(self):
        return self.devisi
    
class Anggota(models.Model):
    nim = models.IntegerField(blank=True, null=True)
    nama = models.CharField(max_length=255)
    alamat = models.TextField(blank=True, null=True)
    tempat_lahir = models.CharField(max_length=255, blank=True, null=True)
    tanggal_lahir = models.DateField()
    jenis_kelamin = models.CharField(max_length=255)
    prodi = models.CharField(max_length=255)
    semester = models.IntegerField()
    devisi = models.ForeignKey(Devisi, on_delete=models.CASCADE)
    keterangan = models.TextField(blank=True, null=True)
    nomor_hp = models.BigIntegerField()
    facebook = models.CharField(max_length=255, blank=True, null=True)
    
    created = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True, null=True)
    
    def __str__(self):
        return self.nama

class ProgramKerja(models.Model):
    nama_program = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nama_program
    
class KalenderKerja(models.Model):
    # id_program = models.IntegerField(null=True)
    nama = models.CharField(max_length=255, blank=True, null=False)
    program = models.ForeignKey(ProgramKerja, on_delete=models.CASCADE)
    tanggal_program = models.DateField()
    lokasi_program = models.CharField(max_length=255)
    deskripsi = models.CharField(max_length=255, blank=True, null=True)

    created = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True, null=True)
    
class HariDiskusi(models.Model):
    hari = models.CharField(max_length=255)
    
    def __str__(self):
        return self.hari
    
class JadwalDiskusi(models.Model):
    hari = models.ForeignKey(HariDiskusi, on_delete=models.CASCADE)
    devisi = models.ForeignKey(Devisi, on_delete=models.CASCADE)
    
    created = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True, null=True)