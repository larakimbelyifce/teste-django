from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def pessoa_view(request):
    return render(request, 'pessoa_view.html', {})