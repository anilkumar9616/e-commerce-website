from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'ind.html')

def analyze(request):
    dj = request.GET.get('text', 'default')
    removepun = request.GET.get('removepun', 'default')

    return HttpResponse("remove pun")


