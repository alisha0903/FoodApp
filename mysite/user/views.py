from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method== 'POST':
        form =UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('usrname')
            messages.success(request,f'welcome {username} your account is created')
            return redirect('food:index')
    else:    
     form=UserCreationForm()
    return render (request,'user/register.html',{'form':form})
 