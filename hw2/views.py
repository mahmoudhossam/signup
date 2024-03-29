from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, Context
from rot13 import rot13
from valid import *

def main(request):
    t = loader.get_template('page.html')
    if request.method == "GET":
        c = Context({})
        return HttpResponse(t.render(c))
    elif request.method == "POST":
        user_input = request.POST['text']
        result = rot13(user_input)
        c = Context({'content': result})
        return HttpResponse(t.render(c))

def signup(request):
    t = loader.get_template('signup.html')
    if request.method == "GET":
        c = Context({})
        return HttpResponse(t.render(c))

    elif request.method == "POST":
        usr = request.POST['username']
        pw = request.POST['password']
        verify = request.POST['verify']
        email = request.POST['email']
        error_occurred = False
        c = {
                'usr': '',
                'usr_val': '',
                'email': '',
                'email_val': '',
                'pw': '',
                'pw_val': '',
                'verify': '',
                'verify_val': ''}
        if not valid_username(usr):
            c['usr'] = "This username is invalid."
            error_occurred = True
        else:
            c['usr_val'] = usr
        if not valid_email(email) and not email.strip() == "":
            c['email'] = "This email is invalid."
            error_occurred = True
        else:
            c['email_val'] = email
        if not valid_password(pw) :
            c['pw'] = "This password is inavlid."
            error_occurred = True
        else:
            c['pw_val'] = pw
        if verify != pw:
            c['verify'] = "These passwords do not match."
            error_occurred = True
        else:
            c['verify_val'] = verify
        if error_occurred:
            return HttpResponse(t.render(Context(c)))
        else:
            return HttpResponseRedirect('/thanks?usr=%s' % usr)

def thanks(request):
    user = request.GET['usr']
    return HttpResponse('Welcome, %s!' % user)
