from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth import authenticate, login, get_user_model
from .forms import ContactForm, LoginForm, RegisterForm
from django.shortcuts import render, redirect

def home_page(request):
   context = {
      "title":"Hello World!",
      "content":"Home page."
       }
   if request.user.is_authenticated:
      context["premium_content"] = "YEAHH"
   return render(request, "home_page.html", context)

def about_page(request):
   context = {
      "title":"Hello World!",
      "content":"About page."
       }
   return render(request, "home_page.html", context)

def contact_page(request):
   contact_form = ContactForm(request.POST or None)
   context = {
      "title":"Hello World!",
      "content":"Contact page.",
      "form": contact_form
       }
   if contact_form.is_valid():
       print(contact_form.cleaned_data)
   #if request.method == "POST":
       #print(request.POST)
       #print(request.POST.get("fullname"))
   return render(request, "contact/view.html", context)

def login_page(request):
   form = LoginForm(request.POST or None)
   context = {
       "form": form
       }
   if form.is_valid():
       #print(form.cleaned_data)
       username = form.cleaned_data.get("username")
       password = form.cleaned_data.get("password")
       user = authenticate(request, username=username, password=password)
       print(user)
       print("user")
       if user is not None:
           #print(request.user.is_authenticated)
           login(request, user)
           #clears out the form after submission
           #context["form"] = LoginForm()
           return redirect("/")
       else:
           print("Error")
   return render(request, "auth/login.html", context)
User = get_user_model()

def register_page(request):
   form = RegisterForm(request.POST or None)
   context = {
    "form": form
    }
   if form.is_valid():
       #print(form.cleaned_data)
       username = form.cleaned_data.get("username")
       email = form.cleaned_data.get("email")
       password = form.cleaned_data.get("password")
       new_user = User.objects.create_user(username, email, password)
   return render(request, "auth/register.html", context)

 #def home_page(request):
 #   return HttpResponse("<h1>Hello World!<h1>")
