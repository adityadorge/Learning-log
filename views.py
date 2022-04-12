from django.shortcuts import render , redirect
from django.urls import reverse
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib import messages
from learning_logs.views import index
from users.forms import UserRegistrationForm

#login
def login_view(request):
	if request.method =='POST':
	       form = AuthenticationForm(request,data=request.POST)
	       username = request.POST.get('username')
	       password = request.POST.get('password') 
	       user = authenticate(request, username = username, password = password)	       	       
	       if form.is_valid():
	       	login(request,user)
	       	return redirect('learning_logs:index')
	else:
	       form =AuthenticationForm()
	return render(request, 'users/login.html', {'form':form})

#logout
def logout_view(request):
	logout(request)
	return render(request, 'learning_logs/index.html')	

#registration
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
#            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('learning_logs:index')
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)

#registration
#def register(request):
#	if request.method =='POST':
#		form = UserCreationForm(data=request.POST)
#		username = request.POST.get('username')
#		password = request.POST.get('password')
#		authenticated_user = authenticate(username=username,password = password)
#		if form.is_valid():
#			new_user = form.save()
#			return HttpResponseRedirect(reverse('learning_logs:index'))
#	else:
#		form = UserCreationForm()
#	return render(request, 'users/register.html', {'form': form})
