from django.shortcuts import render, redirect
from .forms import NotesCreateForm
from .models import Notes


# Create your views here.
def create_view(request):
    form = NotesCreateForm()
    if request.method == "POST":
        form = NotesCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {
        "form": form,
    }
    return render(request, "Create_notes.html", context)

def edit_view(request,pk):
    note = Notes.objects.get(id=pk)
    form = NotesCreateForm(instance=note)
    if request.method == "POST":
        form = NotesCreateForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("/")
        
    context = {
        'form': form
    }
    return render(request, 'Edit.html', context)


def delete_view(request,pk):
    note = Notes.objects.get(id=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('/')
    context = {
       'note': note
    }
    return render(request, 'Delete.html',context)

def read_view(request,pk):
    note = Notes.objects.get(id=pk) 
    context = {
        'notes':note
    }
    return render(request,'Read.html', context)

def home(request):
    obj = Notes.objects.all()
    context = {
        "obj": obj,
    }
    return render(request, "Home.html", context)
