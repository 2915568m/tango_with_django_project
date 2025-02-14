from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage':'Crunchy, creamy, cookie, candie, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return HttpResponse("This is the About page. <a href='/rango/'>Back to Home</a>")