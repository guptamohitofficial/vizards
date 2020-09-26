from django.shortcuts import render, HttpResponseRedirect, redirect
from users.models import User
from django.contrib import messages

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.filter(email=email,password=password)
        if user:
            request.session['fname'] = user[0].fname
            request.session['lname'] = user[0].lname
            request.session['username'] = user[0].username
            request.session['email'] = user[0].email
            return redirect('homepage')
        else:
            messages.info(request, "User not Found")
            return redirect('login')
    return render(request, 'login.html', {'title':'Login - '})

def signup(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        User(fname=fname,lname=lname,username=username,email=email,password=password).save()
        request.session['fname'] = fname
        request.session['lname'] = lname
        request.session['username'] = username
        request.session['email'] = email
        return redirect('homepage')
    return render(request, 'signup.html', {'title':'Signup - '})

def logout(request):
    del request.session['fname']
    del request.session['lname']
    del request.session['username']
    del request.session['email']
    return redirect('homepage')

