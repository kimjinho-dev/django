from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def greeting(request):
    context = {
        'name' : 'alex', 
        'age' : '25', 
        'food' : ['pizza','alcohol'],
    }

    return render(request, 'greeting.html', context)

def base(request):
    return render(request, 'base.html')

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    context = {
        'meg' : request.GET.get('meg'),
        'time' : request.GET.get('time'),
        'num' : request.GET.get('num'),
    }
    return render(request, 'catch.html', context)