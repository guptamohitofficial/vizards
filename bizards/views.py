from django.shortcuts import render
from users.models import User
from cards.models import Card

def homepage(request):
    if request.session.get('username'):
        user = User.objects.filter(username=request.session.get('username'))[0]
        context = {
            'user' : user,
        }
        return render(request, 'home.html', context)
    return render(request, 'index.html')

def create(request):
    card = Card()
    context = {
        'selected' : True,
    }
    return render(request, 'create.html', context)

def savenew(request):
    context = {
        'selected' : True,
    }
    return render(request, 'savenew.html', context)

