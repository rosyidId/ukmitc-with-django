# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from app import models
from django.forms import widgets
from django.utils.regex_helper import Choice

class DaftarForm(forms.Form):
    nim = forms.IntegerField(label="NIM",
        widget=forms.NumberInput(
            attrs={
                "label" : "NIM",
                "placeholder" : "NIM",
                "class" : "form-control"
            }
        ))
    
    nama = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "label" : "Nama",
                "placeholder" : "Nama Lengkap",                
                "class": "form-control "
            }
        ))
    
    alamat = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder" : "Alamat",                
                "class": "form-control",
            }
        ))
    
    tempat_lahir = forms.CharField(label="Tempat Lahir",
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Tempat Lahir",
                "class" : "form-control"
            }
        ))
    
    tanggal_lahir = forms.DateField(label="Tanggal Lahir",
        widget=forms.DateInput(
            attrs={
                "class" : "form-control",
                "type" : "date"
            }
        ))
    
    GENDER = [ 
        ("Laki - laki", "Laki - laki"), 
        ("Perempuan", "Perempuan")
    ]
    
    jenis_kelamin = forms.ChoiceField(label="Jenis Kelamin",
        widget=forms.Select(
            attrs={
                "class" : "form-control"
            },
        ),
        choices=GENDER
    )
    
    PRODI = [
        ("TI", "Teknik Informatika"),
        ("SI", "Sistem Informasi")
    ]
    
    prodi = forms.ChoiceField(label="Program Studi",
        widget=forms.Select(
            attrs={
                "class" : "form-control"
            },
        ),
        choices=PRODI
    )
    
    SEMESTER = [
        ("2", "2"),
        ("4", "4"),
        ("6", "6")
    ]
    
    semester = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                "class" : "form-control"
            },
        ),
        choices=SEMESTER
    )
    
    devisi = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                "class" : "form-control"
            },
        ),
        queryset=models.Devisi.objects.all()
    )
    
    keterangan = forms.CharField(label="Alasan Mengambil Devisi",
        widget=forms.Textarea(
            attrs={
                "placeholder" : "Keterangan",                
                "class": "form-control"
            }
        ))
    
    nomor_hp = forms.IntegerField(label="Nomor HP/WA",
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "ex. 08xxxxxxx",
                "class" : "form-control"
            }
        )
    )
    
    facebook = forms.CharField(required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "isone99",
                "class" : "form-control",
            },
        )
    )

class ProgramForm(forms.Form):
    nama_program = forms.CharField(label="Nama Program ",
        widget=forms.TextInput(
            attrs={           
                "class": "col col-md-6 form-control",
            }
        ))
    
class KalenderForm(forms.Form):
    nama = forms.CharField(label="Nama Program ",
        widget=forms.TextInput(
            attrs={           
                "class": "form-control",
            }
        ))
    
    program = forms.ModelChoiceField(label="Jenis Program ",
        widget=forms.Select(
            attrs={
                "class" : "form-control"
            },
        ),
        queryset = models.ProgramKerja.objects.all()
    )
    
    tanggal_program = forms.DateField(label='Tanggal Agenda ',
        widget=forms.DateInput(
            attrs={
                "class" : "col col-md-6 form-control",
                "type" : "date",
                "id" : "datetimepicker1",
            },
        )
    )
    
    lokasi_program = forms.CharField(label="Lokasi Agenda ",
        widget=forms.TextInput(
            attrs={
                "class" : "form-control",
            }
        )
    )
    
    deskripsi = forms.CharField(label="Deskripsi ",
        widget=forms.Textarea(
            attrs={
                "class" : "form-control",
            }
        )
    )
    
class JadwalForm(forms.Form):
    hari = forms.ModelChoiceField(label="Malam Diskusi",
        widget=forms.Select(
            attrs={
                'class' : 'form-control'
            }
        ),
        
        queryset=models.HariDiskusi.objects.all()
    )
    
    devisi = forms.ModelChoiceField(label="Materi",
        widget=forms.Select(
            attrs={
                'class' : 'form-control'
            }
        ),
        queryset=models.Devisi.objects.all()
    )