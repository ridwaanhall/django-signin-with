from django.shortcuts import render

# Create your views here.

def home(request):
    """
    Home page view - displays the hello world landing page
    """
    context = {
        'title': 'Hello World',
        'message': 'Welcome to Django Social!'
    }
    return render(request, 'base/home.html', context)
