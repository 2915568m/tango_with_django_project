from django.shortcuts import render

def index(request):
    context_dict = {'boldmessage':'Crunchy, creamy, cookie, candie, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)