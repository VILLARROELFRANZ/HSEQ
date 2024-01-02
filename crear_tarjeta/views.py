from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import TarjetaHSEQ
from .forms import TarjetaHSEQForm

@login_required
def lista_tarjetas(request):
    tarjetas = TarjetaHSEQ.objects.all()  
    return render(request, 'lista_tarjetas.html', {'tarjetas': tarjetas})

@login_required
def crear_tarjeta(request):
    if request.method == 'GET':
        form = TarjetaHSEQForm()
        return render(request, 'crear_tarjeta.html', {'form': form})
    else:
        form = TarjetaHSEQForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tarjetas')
        else:
            return render(request, 'crear_tarjeta.html', {'form': form})

@login_required
def detalle_tarjeta(request, pk):
    tarjeta = get_object_or_404(TarjetaHSEQ, pk=pk)
    if request.method == 'POST':
        form = TarjetaHSEQForm(request.POST, instance=tarjeta)
        if form.is_valid():
            form.save()
            return redirect('lista_tarjetas')
    else:
        form = TarjetaHSEQForm(instance=tarjeta)
        return render(request, 'detalle_tarjeta.html', {'tarjeta': tarjeta, 'form': form})

@login_required
def editar_tarjeta(request, pk):
    tarjeta = get_object_or_404(TarjetaHSEQ, pk=pk)
    if request.method == 'POST':
        form = TarjetaHSEQForm(request.POST, instance=tarjeta)
        if form.is_valid():
            form.save()
            return redirect('lista_tarjetas')
    else:
        form = TarjetaHSEQForm(instance=tarjeta)
        return render(request, 'editar_tarjeta.html', {'form': form, 'tarjeta': tarjeta})

@login_required
def cerrar_tarjeta(request, pk):
    tarjeta = get_object_or_404(TarjetaHSEQ, pk=pk)
    if request.method == 'POST':
        tarjeta.observacion_cerrada = True
        tarjeta.observacion_abierta = False
        tarjeta.save()
        return redirect('lista_tarjetas')

@login_required
def eliminar_tarjeta(request, pk):
    tarjeta = get_object_or_404(TarjetaHSEQ, pk=pk)
    if request.method == 'POST':
        tarjeta.delete()
        return redirect('lista_tarjetas')
    else:
        return redirect('lista_tarjetas')


def crear_tarjeta_publico(request):
    if request.method == 'POST':
        form = TarjetaHSEQForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirigir a la página de confirmación
            return redirect('confirmacion_envio')
    else:
        form = TarjetaHSEQForm()

    return render(request, 'crear_tarjeta_solo.html', {'form': form})

def confirmacion_envio(request):
    return render(request, 'confirmacion_envio.html')


