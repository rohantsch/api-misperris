from django.shortcuts import render
from django.http import HttpResponse
from .models import Persona, Mascotas
from django.shortcuts import redirect
from django.template.loader import get_template 
# Create your views here.

#importar user
from django.contrib.auth.models import User
#sistema de autenticación 
from django.contrib.auth import authenticate,logout, login as auth_login

from django.contrib.auth.decorators import login_required

def administrar(request):
    return render(request, 'admin.html',{'Listado_registro':Mascotas.objects.all(), 'personas': Persona.objects.all()})

def galeria(request):
    return render(request, 'galeria.html',{'Listado_registro':Mascotas.objects.all()})

def manifest(request):
    return render(request, 'manifest.json', )


def registPerro(request):

    fotografia = request.FILES.get('fotografia', False)
    nombre_mascota = request.POST.get('nombreMascota', '')
    raza_predominante = request.POST.get('razaPredominante', '')
    descripcion = request.POST.get('descripcion', '')
    estado = request.POST.get('estado', '')

    mascota = Mascotas(fotografia = fotografia, nombre_mascota = nombre_mascota, raza_predominante = raza_predominante, descripcion = descripcion,
                       estado =estado)

    mascota.save()

    return render(request, 'admin.html', {})

def editPerro(request):

    id_mascota = request.POST.get('modificarIdMascota', '')
    mascota = Mascotas.objects.get(pk = id_mascota)

    fotografia = request.POST.get('modificarFotografia', False)
    nombre_mascota = request.POST.get('modificarNombreMascota', '')
    raza_predominante = request.POST.get('modificarRazaPredominante', '')
    descripcion = request.POST.get('modificarDescripcion', '')
    estado = request.POST.get('modifcarEstado', '')

    mascota.fotografia = fotografia
    mascota.nombre_mascota = nombre_mascota
    mascota.raza_predominante = raza_predominante
    mascota.descripcion = descripcion
    mascota.estado = estado

    mascota.save()

    return render(request, 'admin.html', {})

def index(request):
    user = request.session.get('user',None)
    return render(request,'index.html',{'name':'Registro de personas','personas':Persona.objects.all(),'user':user})



def crear(request):


    run = request.POST.get('run','')
    nombre = request.POST.get('nombre','')
    fecha = request.POST.get('fecha','')
    correo = request.POST.get('correo','')
    telefono = request.POST.get('telefono','')
    region = request.POST.get('region','')
    comuna = request.POST.get('comuna','')
    vivienda = request.POST.get('viviendo','')
    contrasenia = request.POST.get('contrasenia', '')

    persona = Persona(run=run, nombre=nombre, fecha=fecha, correo=correo, telefono=telefono, region=region, comuna=comuna, vivienda=vivienda, contrasenia=contrasenia)
    persona.save()    
    

    return redirect('index')

@login_required(login_url='login')
def eliminar(request,id):
    persona = Persona.objects.get(pk = id)
    persona.delete()
    return redirect('index')

@login_required(login_url='login')
def editar(request):
    nombre = request.POST.get('nombre','')
    correo = request.POST.get('correo','')
    id = request.POST.get('id',0)
    persona = Persona.objects.get(pk = id)
    persona.nombre = nombre
    persona.correo = correo
    persona.save()
    return redirect('index')

def cerrar_session(request):
    del request.session['usuario']
    return redirect('index')

def login(request):
    return render(request,'login.html',{})

def login_iniciar(request):
    username = request.POST.get('nombre_usuario', '')
    password = request.POST.get('contrasenia', '')
    user = authenticate(request, username = username ,password = password)
    print(user)
    if user is not None:
       auth_login(request, user)
       return redirect('index')
    else:
        return HttpResponse('No existe html')

def sw(request, js):
      template = get_template('sw.js')
      html = template.render()
      return HttpResponse(html, content_type="application/x-javascript")

def shell_sworker(request):
    return render(request,'shell.html',{})

def shell_admin(request):
    return render(request,'shelladmin.html',{})

def shell_galeria(request):
    return render(request,'shellgaleria.html',{})

def shell_log(request):
    return render(request,'shelllog.html',{})