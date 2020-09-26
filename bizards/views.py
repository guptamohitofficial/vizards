from django.shortcuts import render
from users.models import User

def homepage(request):
    if request.session.get('username'):
        user = User.objects.filter(username=request.session.get('username'))[0]
        context = {
            'user' : user,
        }
        return render(request, 'home.html', context)
    return render(request, 'index.html')