from django.shortcuts import render,redirect
from django.http import HttpResponse
from user.forms import SignupForm
from django.contrib.auth import login,logout

from user.forms import LoginForm

def signin(request):
    if request.method == "POST":
      login_form = LoginForm(request.POST)
      data={
        'login_form':login_form
      }
      print(login_form.is_valid())
      print(login_form.error_messages)
      
      if(login_form.is_valid()):
        user = login_form.save()
        login(request, user)
        return redirect('/')
      else:
        return render(request,'auth/login.html',{"data":data})
    else:
      login_form = LoginForm()
      data={
        'login_form':login_form
      }
      return render(request,'auth/login.html',{"data":data})

def signup(request):
  if request.method == "POST":
    signup_form = SignupForm(request.POST)
    data={
      'signup_form':signup_form
    }
    if(signup_form.is_valid()):
      user = signup_form.save()
      login(request, user)
      return redirect('/')
    else:
      return render(request,'auth/signup.html',{"data":data})
  else:
    signup_form = SignupForm()
    data={
      'signup_form':signup_form
    }
    return render(request,'auth/signup.html',{"data":data})

def sign_out(request):
  logout(request)
  return redirect('users/signin')