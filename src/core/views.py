from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from django.contrib.sites.shortcuts import get_current_site
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.http import HttpResponse, Http404
from .models import Profile
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response


from .forms import SignupForm
# Create your views here.

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            context = {
                'message': 'user saved successfully'
            }
            return Response(context, status=status.HTTP_201_CREATED)            
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def profile(request):
    current_user = request.user
    user = User.objects.get(pk=current_user.id)
    profile = Profile.objects.filter(user=user).get()

    if not profile.email_confirmed:
        messages.success(request, f'Account is created for {profile.user}! to need to confirm your email before login')
        return redirect('login')
    
    context = {
        "profile": profile
    }
    return render(request, 'profile.html', context)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))

        user = User.objects.get(pk=uid)
        profile = Profile.objects.filter(user=user).get()
        
        if(user.profile.token == profile.token):
            profile.refresh_from_db()
            profile.is_active = True
            profile.email_confirmed = True
            profile.save()
            context = {
                "message": "Thank you for your email confirmation. Now you can login your account."
            }
            return render(request, 'core/send_email.html', context)
        else:
            context = {
                "message": "access denied."
            }
            return render(request, 'core/send_email.html', context)
        
    except(TypeError, ValueError, OverflowError):
        user = None
        return HttpResponse('Activation link is invalid!')
