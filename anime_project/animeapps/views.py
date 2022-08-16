

from datetime import datetime
from multiprocessing import context
from re import template



from animeapps.models import AppUser
from django.shortcuts import render
from django.core.mail import send_mail
from animeapps.forms import RegistrationForm,LoginForm,OtpForm

# Create your views here.
def home(request):
    
    template = 'home.html','front/css.css',

    return render(request,template)
def login(request):
    lf = LoginForm()
    
    template = 'users/login.html'
    if request.method == "POST":
        user = AppUser.objects.get(email=request.POST.get('email'))
        if request.POST.get('password') == user.password:
            request.session['user_email'] = user.email
            if request.session.has_key('user_email'):
               
            
                template = 'anime-name.html'
                
                return render(request,template)
            
        else:
            context = {
                'form': lf,
                'msg_error' : 'Invalid User Id or Password'
            }
            return render(request,template,context)
    else:
        context = {'form': lf}
        return render(request,template,context)





def registration(request):
    rf = RegistrationForm()
    
    template = 'users/create.html'
    if request.method == "POST":
        user = AppUser()
        user.first_name = request.POST.get('first_name')
        user.middle_name = request.POST.get('middle_name')
        user.last_name = request.POST.get('last_name')
        user.contact = request.POST.get('contact')
        user.email = request.POST.get('email')
        user.dob = request.POST.get('dob')
        user.password = request.POST.get('password')
        user.address = request.POST.get('address')
        user.created_at = datetime.now()
        user.save()
        send_mail(
            'Sticker - Zone Verification Code',
            "your Verification code for Sticker-Zone is: 1123",
            'rabintwana18@gmail.com',
            [user.email],
            fail_silently=False,
        )

        
        context = {
            'form':rf,
            'success' : 'Registered Successfully',
            'login' : 'Please login using  this registered Email'
            
                    }
        return render(request,template,context)
    else:
        context = {
            'form':rf,
        }
        return render(request,template,context)
def naruto(request):
    lf = LoginForm()
    if request.session.has_key('user_email'):
        template = 'anime/naruto.html'
        return render(request,template)
    else:
        template = 'users/login.html'
        context = {
                'form' : lf,
                'msg_error' : 'Please Login First'
            }
        return render(request,template,context)

def user_logout(request):
    del request.session['user_email']
    template = "users/login.html"
    lf = LoginForm()
    context = {
        'form' : lf,
        'msg_error':"Please Login"
    }
    return render(request,template,context)

def user_otp(request):
    vf = OtpForm()
    
    if request.method == "POST":
       template = 'users/otp.html'
       context = {
        'form' : vf,
       }
       return render(request,template,context)
            






        



