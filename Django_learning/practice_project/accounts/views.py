from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
# Create your views here.
def registration(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        user = User.objects.create_user(username=username,password=password1,email=email,last_name=lastname,first_name = firstname)
        user.save()
        print("User created")
        return redirect('/')
    else:
        return render(request,'accounts/registration.html')
