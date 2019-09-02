from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm, RegistrationForm, LoginForm, SelectionForm, DuesForm, NoDuesForm
from django.http import HttpResponse, Http404
from selection.models import Student, Room, Hostel
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from pprint import pprint
from django.contrib.auth import get_user_model


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False           
            token = account_activation_token.make_token(user)            
            user.token = token
            user = form.save()
            user.refresh_from_db()         
            Student.objects.create(user=user)           

            user = form.save()

            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
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
            return HttpResponse('Please confirm your email address to complete the registration')
            
            # Student.objects.create(user=new_user)
        #     cd = form.cleaned_data
        #     user = authenticate(
        #         request,
        #         username=cd['username'],
        #         password=cd['password1'])
        #     if user is not None:
        #         if user.is_active:
        #             login(request, user)
        #             return redirect('login/edit/')
        #         else:
        #             return HttpResponse('Disabled account')
        #     else:
        #         return HttpResponse('Invalid Login')
    else:
        form = UserForm()
        args = {'form': form}
        return render(request, 'reg_form.html', args)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd['username'],
                password=cd['password'])

            print(user)      
            
            if user is not None:
                # return HttpResponse('inside user page')
                if user.is_active:           
                    if user.is_warden:
                        return HttpResponse('I am inside warden page')
                    else:
                        login(request, user)
                        student = request.user.student
                        return render(request, 'profile.html', {'student': student})
                        #return HttpResponse('I am inside login page')
                else:
                    return HttpResponse('Disabled account')
            # else:
            #     return HttpResponse('user not logged in')
            # else:
            #     return HttpResponse('Invalid Login from user')
                # login(request, user)
                # student = request.user.student
                # return render(request, 'profile.html', {'student': student})
            
            else:
                print(user)
                return HttpResponse('Invalid Login from user')    
                
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})   


def warden_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd['username'],
                password=cd['password'])
            if user is not None:
                if not user.is_warden:
                    return HttpResponse('Invalid Login')
                elif user.is_active:
                    login(request, user)
                    room_list = request.user.warden.hostel.room_set.all()
                    context = {'rooms': room_list}
                    return render(request, 'warden.html', context)
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid Login')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


@login_required
def edit(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, instance=request.user.student)
        if form.is_valid():
            form.save()
            student = request.user.student
            return render(request, 'profile.html', {'student': student})
    else:
        form = RegistrationForm(instance=request.user.student)
        return render(request, 'edit.html', {'form': form})


@login_required
def select(request):
    if request.user.student.room:
        room_id_old = request.user.student.room_id
        # print(room_id_old)

    if request.method == 'POST':
        if not request.user.student.no_dues:
            return HttpResponse('You have dues. Please contact your Hostel Caretaker or Warden')
        form = SelectionForm(request.POST, instance=request.user.student)
        if form.is_valid():
            if request.user.student.room_id:
                request.user.student.room_allotted = True
                r_id_after = request.user.student.room_id
                room = Room.objects.get(id=r_id_after)
                room.vacant = False
                room.save()
                try:
                    room = Room.objects.get(id=room_id_old)
                    room.vacant = True
                    room.save()
                except BaseException:
                    pass
            else:
                request.user.student.room_allotted = False
                try:
                    room = Room.objects.get(id=room_id_old)
                    room.vacant = True
                    room.save()
                except BaseException:
                    pass
            form.save()
            student = request.user.student
            return render(request, 'profile.html', {'student': student})
    else:
        # room_details = get_object_or_404(Room, id=room_id_old)
        room_detail = get_object_or_404(Room, id=room_id_old)

        context = {
            "room_detail": room_detail
        }

        if not request.user.student.no_dues:
            return HttpResponse('You have dues. Please contact your Hostel Caretaker or Warden')
        
        form = SelectionForm(instance=request.user.student)

        student_gender = request.user.student.gender
        student_course = request.user.student.course
        student_room_type = request.user.student.course.room_type
        # print(student_room_type)
        hostel = Hostel.objects.filter(
            gender=student_gender, course=student_course)

        # print(hostel);

        x = Room.objects.none()       

        if student_room_type == 'B':
            # for i in hostel:
            for i in range(len(hostel)):
                # print(i)
                h_id = hostel[i].id
                a = Room.objects.filter(
                    hostel_id=h_id, room_type=['S', 'D'], vacant=True)
                # pprint(a)
                x = x | a
                # print(x)
        else:
            # pprint(hostel)
            for i in range(len(hostel)):
                
                h_name = hostel[i].name

                pprint(h_name)
                
                a = Room.objects.filter(vacant=True)

                pprint(a)

                x = x | a

        form.fields["room"].queryset = x

        # print(form.fields["room"].queryset)
        return render(request, 'select_room.html', {'form': form})


@login_required
def warden_dues(request):
    user = request.user
    if user is not None:
        if not user.is_warden:
            return HttpResponse('Invalid Login')
        else:
            students = Student.objects.all()
            return render(request, 'dues.html', {'students': students})
    else:
        return HttpResponse('Invalid Login')


@login_required
def warden_add_due(request):
    user = request.user
    if user is not None:
        if not user.is_warden:
            return HttpResponse('Invalid Login')
        else:
            if request.method == "POST":
                form = DuesForm(request.POST)
                if form.is_valid():
                    student = form.cleaned_data.get('choice')
                    student.no_dues = False
                    student.save()
                    return HttpResponse('Done')
            else:
                form = DuesForm()
                return render(request, 'add_due.html', {'form': form})
    else:
        return HttpResponse('Invalid Login')


@login_required
def warden_remove_due(request):
    user = request.user
    if user is not None:
        if not user.is_warden:
            return HttpResponse('Invalid Login')
        else:
            if request.method == "POST":
                form = NoDuesForm(request.POST)
                if form.is_valid():
                    student = form.cleaned_data.get('choice')
                    student.no_dues = True
                    student.save()
                    return HttpResponse('Done')
            else:
                form = NoDuesForm()
                return render(request, 'remove_due.html', {'form': form})
    else:
        return HttpResponse('Invalid Login')


def logout_view(request):
    logout(request)
    return redirect('/')


def BH5_Floor1(request):
    room_list = Room.objects.order_by('name')
    room_dict = {'rooms':room_list}
    return render(request, 'BH5_Floor1.html', context=room_dict)


def BH5_Floor2(request):
    room_list = Room.objects.order_by('name')
    room_dict = {'rooms':room_list}
    return render(request, 'BH5_Floor2.html', context=room_dict)


def BH5_Floor3(request):
    room_list = Room.objects.order_by('name')
    room_dict = {'rooms':room_list}
    return render(request, 'BH5_Floor3.html', context=room_dict)


def BH5_Floor4(request):
    room_list = Room.objects.order_by('name')
    room_dict = {'rooms':room_list}
    return render(request, 'BH5_Floor4.html', context=room_dict)


def BH5_Floor5(request):
    room_list = Room.objects.order_by('name')
    room_dict = {'rooms':room_list}
    return render(request, 'BH5_Floor5.html',context=room_dict)


def BH5_Floor6(request):
    room_list = Room.objects.order_by('name')
    room_dict = {'rooms':room_list}
    return render(request, 'BH5_Floor6.html', context=room_dict)


def BH5_GroundFloor(request):
    room_list = Room.objects.order_by('name')
    room_dict = {'rooms':room_list}
    return render(request, 'BH5_GroundFloor.html', context=room_dict)


def hostel_detail_view(request, hostel_name):
    try:
        this_hostel = Hostel.objects.get(name=hostel_name)
    except Hostel.DoesNotExist:
        raise Http404("Invalid Hostel Name")
    context = {
        'hostel': this_hostel,
        'rooms': Room.objects.filter(
            hostel=this_hostel)}
    return render(request, 'hostels.html', context)



    # if user is not None:
        
    #     # return redirect('home')and account_activation_token.check_token(user, token):
    #     return HttpResponse('Activation link is invalid!')
    # else:
        
    #     # login(request, user)
    #     print(user)
    #     print(user.is_active)
    #     return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
        