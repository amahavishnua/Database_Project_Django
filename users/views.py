from django.shortcuts import render,redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegForm
# Create your views here.
def register(request):
	if request.method =='POST':
		form=UserRegForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username') #this is dictionary 
			messages.success(request,f'Account created for {username}')
			return redirect('WDS-home')
	else:
		form =UserRegForm()
	return render(request,'users/register.html',{'form':form})

'''
message.debug
message.info
message.success
message.warning
message.error'''