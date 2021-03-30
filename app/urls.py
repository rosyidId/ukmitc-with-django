# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views, grafik

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('anggota', views.anggota, name='anggota'),
    path('anggota/daftar', views.daftar, name='daftar'),
    path('anggota/update/<int:pk>', views.edit, name='edit'),
    path('anggota/detail/<int:pk>', views.detail, name='detail'),
    path('anggota/delete/<int:pk>', views.delete, name='delete'),
    path('anggota/devisi/<int:id>', views.anggota_devisi, name='devisi'),
    
    path('proker', views.proker_list, name='prokerList'),
    path('proker/create', views.proker_create, name='prokerCreate'),
    path('kalender', views.kalender_list, name='kalenderList'),
    path('kalender/<int:id>', views.program_kalender, name="kalenderProgram"),
    path('kalender/create', views.kalender_create, name='kalenderCreate'),
    
    path('AnggotaByDevisi', grafik.AnggotaByDevisi.as_view()),
    path('anggotaByDevisi', grafik.AnggotaByDevisi.as_view()),
    
    path('jadwal/create', views.jadwal_create, name="jadwalCreate"),
    path('jadwal', views.jadwal_list, name="jadwalList"),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
