from django.shortcuts import render, redirect
from .forms import EForm
from .models import Employee


def home(request):
    form = EForm ()
    if request.method == 'GET':
        form = EForm (request.GET)
        if form.is_valid ():
            form.save ()
            return redirect ('/')
        else:
            pass

    return render (request, 'emp/home.html', {'form': form})


def show(request):
    form = Employee.objects.all ()
    form = {
        'form': form
    }

    return render (request, 'emp/show.html', form)


def delete(request, id):
    form = Employee.objects.get (pk=id)
    form.delete ()
    return redirect (show)


def edit(request, id):
    form = Employee.objects.get (pk=id)
    form = EForm (instance=form)

    return render (request, 'emp/edit.html', {'form': form,'id':id})


def update(request, id):
    employee = Employee.objects.get (pk=id)
    form = EForm (request.POST, instance=employee)
    if form.is_valid ():
        form.save ()
        return redirect ("/show")
    return render (request, 'edit.html', {'employee': employee,'id':id})