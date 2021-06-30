from django.shortcuts import render, redirect
from .models import UrlRepository, Commit, ModifiedFile
from pydriller import Repository
from .forms import UrlRepositoryForm


def index(request):
    error = ''
    if request.method == 'POST':
        form = UrlRepositoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('results/')
        else:
            error = 'Данные не введены'

    form = UrlRepositoryForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'integrate/index.html', data)


def results(request):
    return render(request, 'integrate/results.html')
