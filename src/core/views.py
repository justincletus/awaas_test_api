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


from core.forms import SignupForm
# Create your views here.

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        # print(form)
        if form.is_valid():
            
            user           = form.save()
            # print(user) 
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')

            # user = authenticate(username=username, password=raw_password)
            
            user.refresh_from_db()
            
            user.profile.is_active = False            

            token = account_activation_token.make_token(user)             
            user.profile.token = token
            user.is_active = False           
            user.profile.save()
            print(user.profile.token)
            # user.refresh_from_db()
            
            current_site = get_current_site(request)
            # print(current_site)
            mail_subject = 'Activate your account.'
            message = render_to_string('core/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':token,
            })
            
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            
            email.send()
            context = {
                "messages": "Please confirm your email address to complete the registration."
            }
            return render(request, 'core/send_email.html', context)

            #return HttpResponse('Please confirm your email address to complete the registration')
            # login(request, user)
            # messages.success(request, f'Account is created for {username}!')
            # return redirect('login')
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
                "messages": "Thank you for your email confirmation. Now you can login your account."
            }
            return render(request, 'core/send_email.html', context)
        else:
            context = {
                "messages": "access denied."
            }
            return render(request, 'core/send_email.html', context) 
           
        
    except(TypeError, ValueError, OverflowError):
        user = None
        return HttpResponse('Activation link is invalid!')

        