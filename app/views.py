from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from app.models import Anggota, Devisi, ProgramKerja, KalenderKerja, JadwalDiskusi
from app import forms

@login_required(login_url="/login/")
def index(request):
    
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    
    try:
        
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def anggota(request):
    data = Anggota.objects.all()
    context = {
        'title' : 'Daftar Anggota',
        'object_list' : data
    }
    template_name = 'anggota/anggota_list.html'
    return render(request, template_name, context)

@login_required(login_url="/login/")
def anggota_devisi(request, id):
    data = Anggota.objects.filter(devisi_id=id)
    context = {
        'title' : 'Daftar Anggota',
        'object_list' : data
    }
    template_name = 'anggota/anggota_list.html'
    return render(request, template_name, context)

@login_required(login_url="/login/")
def daftar(request):
    form = forms.DaftarForm(request.POST or None)
    if form.is_valid():
        anggota = Anggota()
        anggota.nim = form.cleaned_data.get('nim')
        anggota.nama = form.cleaned_data.get('nama')
        anggota.alamat = form.cleaned_data.get('alamat')
        anggota.tempat_lahir = form.cleaned_data.get('tempat_lahir')
        anggota.tanggal_lahir = form.cleaned_data.get('tanggal_lahir')
        anggota.jenis_kelamin = form.cleaned_data.get('jenis_kelamin')
        anggota.prodi = form.cleaned_data.get('prodi')
        anggota.semester = form.cleaned_data.get('semester')
        anggota.devisi = form.cleaned_data.get('devisi')
        anggota.keterangan = form.cleaned_data.get('keterangan')
        anggota.nomor_hp = form.cleaned_data.get('nomor_hp')
        anggota.facebook = form.cleaned_data.get('facebook')
        
        anggota.save()
        return redirect('anggota')
    template_name = 'anggota/anggota_form.html'
    return render(request, template_name, {'form': form})

@login_required(login_url="/login/")
def edit(request, pk):
    anggota = get_object_or_404(Anggota, pk=pk)
    form = forms.DaftarForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('anggota')
    template_name = 'anggota/anggota_form.html'
    return render(request, template_name, {'form': form})

@login_required(login_url="/login/")
def delete(request, pk):
    anggota = get_object_or_404(Anggota, pk=pk)
    if request.method=='POST':
        anggota.delete()
        return redirect('anggota')
    
    template_name='anggota/anggota_delete.html'
    return render(request, template_name, {'object': anggota})

@login_required(login_url="/login/")
def detail(request, pk): 
    data = get_object_or_404(Anggota, pk=pk)
    context = {
        'object' : data
    } 

    template_name = 'anggota/anggota_detail.html'
    return render(request, template_name, context)

@login_required(login_url="/login/")
def proker_list(request):
    data = ProgramKerja.objects.all()
    context = {
        'proker_list' : data
    }
    
    template_name = "includes/sidebar.html"
    return render(request, template_name, context)

@login_required(login_url="/login/")
def proker_create(request):
    form = forms.ProgramForm(request.POST or None)
    if form.is_valid():
        program = ProgramKerja()
        program.nama_program = form.cleaned_data.get('nama_program')
        program.save()
        
        return redirect('prokerList')
    
    template_name = 'proker/proker_form.html'
    return render(request, template_name, {'form':form})

@login_required(login_url="/login/")
def proker_edit(request, pk):
    proker = get_object_or_404(ProgramKerja, pk=pk)
    form = forms.ProgramForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('prokerList')
    template_name = 'proker/proker_form.html'
    return render(request, template_name, {'form': form})

@login_required(login_url="/login/")
def kalender_list(request):
    data = KalenderKerja.objects.all().order_by('tanggal_program')
    context = {
        'kalender_list' : data
    }
    
    template_name = 'proker/kalender_list.html'
    return render(request, template_name, context)

@login_required(login_url="/login/")
def kalender_create(request):
    form = forms.KalenderForm(request.POST or None)
    if form.is_valid():
        kalender = KalenderKerja()
        kalender.nama = form.cleaned_data.get('nama')
        kalender.program = form.cleaned_data.get('program')
        kalender.tanggal_program = form.cleaned_data.get('tanggal_program')
        kalender.lokasi_program = form.cleaned_data.get('lokasi_program')
        kalender.deskripsi = form.cleaned_data.get('deskripsi')
        kalender.save()
        return redirect('kalenderList')
    
    template_name = 'proker/kalender_form.html'
    return render(request, template_name, {'form':form})

def program_kalender(request, id):
    data = KalenderKerja.objects.filter(program_id=id)
    context = {
        'kalender_list' : data
    }
    
    template_name = 'proker/kalender_list.html'
    return render(request, template_name, context)

@login_required(login_url="/login/")
def jadwal_list(request):
    data = JadwalDiskusi.objects.all()
    context = {
        'title' : "Jadwal Diskusi",
        'object_list' : data
    }
    
    template_name = 'jadwal/jadwal_list.html'
    return render(request, template_name, context)
    

@login_required(login_url="/login/")
def jadwal_create(request):
    form = forms.JadwalForm(request.POST or None)
    if form.is_valid():
        jadwal = JadwalDiskusi()
        jadwal.hari = form.cleaned_data.get('hari')
        jadwal.devisi = form.cleaned_data.get('devisi')
        jadwal.save()
        return redirect('jadwalList')
    
    template_name = 'jadwal/jadwal_form.html'
    return render(request, template_name, {'form':form})


@login_required(login_url="/login/")
def jadwal_delete(request, pk):
    jadwal = get_object_or_404(JadwalDiskusi, pk=pk)
    
    if request.method=='POST':
        jadwal.delete()
        return redirect('jadwalList')
    
    template_name='jadwal/jadwal_delete.html'
    return render(request, template_name, {'object': jadwal})