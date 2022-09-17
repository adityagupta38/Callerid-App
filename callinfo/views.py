from django.shortcuts import render, redirect, HttpResponse
from .forms import UserForm, UserLoginForm, GlobalUsersForm, SearchByNameForm, SearchByNumberForm
from django.contrib import messages
from .utils import is_user_authenticated, phoneno_registered
from .models import GlobalUsers, User
from django.db.models import Q

# Create your views here.


def user_login(request):
    if request.method == 'POST':
        phoneno = request.POST.get('phoneno')
        password = request.POST.get('password')
        userform = UserLoginForm(request.POST)
        if not phoneno_registered(phoneno):
            error = 'Phoneno is Not Registerd Pls Register First'
            return render(request, 'user_login.html', {'form': userform, 'error': error})
        if is_user_authenticated(phoneno, password):
            return redirect('/userhome')
        error = 'Invalid Password Pls Enter Correct Password'
        return render(request, 'user_login.html', {'form': userform, 'error': error})
    userloginform = UserLoginForm()
    return render(request, 'user_login.html', {'form': userloginform})


def user_registeration(request):
    if request.method == 'POST':
        phoneno = request.POST['phoneno']
        userform = UserForm(request.POST)
        if phoneno_registered(phoneno=phoneno):
            msg = f'{phoneno} Is Already Registerd Pls Login to Continue'
            return render(request, 'user_registration_form.html', {'form': userform, 'msg': msg})
        if userform.is_valid():
            phoneno = userform.cleaned_data.get('phoneno')
            userform.save()
            msg = f'{phoneno} is Successfully Registered'
            messages.add_message(request, messages.SUCCESS, msg)
            return redirect('/')
        return render(request, 'user_registration_form.html', {'form': userform, 'errors': userform.errors})
    userform = UserForm()
    return render(request, 'user_registration_form.html', {'form': userform})


def user_home(request):
    return render(request, 'user_home.html')


def global_user(request):
    if request.method == 'POST':
        globaluserform = GlobalUsersForm(request.POST)
        if globaluserform.is_valid():
            phoneno = globaluserform.cleaned_data.get('phoneno')
            globaluserform.save()
            msg = f'{phoneno} is Added Successfully'
            globaluser = GlobalUsersForm()
            return render(request, 'global_users_form.html', {'form': globaluser, 'msg': msg})
        return render(request, 'global_users_form.html', {'form': globaluserform, 'errors': globaluserform.errors})
    globaluser = GlobalUsersForm()
    return render(request, 'global_users_form.html', {'form': globaluser})


def search_by_name(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        exist = GlobalUsers.objects.filter(Q(name__startswith=name) | Q(name__contains=name)).order_by('name')
        if exist:
            return render(request, 'searcby_name_result.html', {'phone_list': exist})
        nameform = SearchByNameForm()
        error = "Sorry We Didn't Have An Update For This Name"
        return render(request, 'searchby_name_page.html', {'form': nameform, 'error': error})
    nameform = SearchByNameForm()
    return render(request, 'searchby_name_page.html', {'form': nameform})


def search_by_number(request):
    if request.method == 'POST':
        phoneno = request.POST.get('phoneno')
        if phoneno_registered(phoneno):
            user = User.objects.get(phoneno=phoneno)
            return render(request, 'searchby _number_result.html', {'user': user})
        exist = GlobalUsers.objects.filter(phoneno=phoneno)
        if exist:
            return render(request, 'searchby _number_result.html', {'phone_list': exist, 'user': None})
        numform = SearchByNumberForm()
        error = "Sorry We Didn't Have An Update For This Number"
        return render(request, 'searchby_number_page.html', {'form': numform, 'error': error})
    numform = SearchByNumberForm()
    return render(request, 'searchby_number_page.html', {'form': numform})


def add_update_spam(request):
    if request.method == 'POST':
        phoneno = request.POST.get('phoneno')
        spam = request.POST.get('spam')
        if phoneno_registered(phoneno):
            user = User.objects.get(phoneno=phoneno)
            user.spam = spam
            user.save()
            exist = GlobalUsers.objects.filter(phoneno=phoneno)
            if exist:
                exist.update(spam=spam)
            globaluser = GlobalUsers(name='', phoneno=phoneno, spam=spam)
            globaluser.save()
            return render(request, 'add_spam_no.html', {'msg': f'{phoneno} Added To Spam'})
        exist = GlobalUsers.objects.filter(phoneno=phoneno)
        if exist:
            exist.update(spam=spam)
            return render(request, 'add_spam_no.html', {'msg': f'{phoneno} Added To Spam'})
        globaluser = GlobalUsers(name='', phoneno=phoneno, spam=spam)
        globaluser.save()
        return render(request, 'add_spam_no.html', {'msg': f'{phoneno} Added To Spam'})
    return render(request, 'add_spam_no.html')


def user_logout(request):
    return redirect('/')
