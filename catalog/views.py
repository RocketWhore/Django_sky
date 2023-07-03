from django.shortcuts import render

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name}\n{email}\n{message}')
    return render(request, 'catalog/index.html')

def home(request):
    if request.method == 'GET':
        # name = request.POST.get('name')
        # email = request.POST.get('email')
        # message = request.POST.get('message')
        # print(f'{name}\n{email}\n{message}')
        return render(request, 'catalog/home.html')