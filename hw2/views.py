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
    if request.method == "GET":
        t = loader.get_template('signup.html')
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
                'email': '',
                'pw': '',
                'verify': ''}
        if not valid_username(usr):
            c['usr'] = "This username is invalid."
            error_occurred = True
        if not valid_email(email):
            c['email'] = "This email is invalid."
            error_occurred = True
        if not valid_password(pw) and pw.strip() != "":
            c['pw'] = "This password is inavlid."
            error_occurred = True
        if verify != pw:
            c['verify'] = "These passwords do not match."
            error_occurred = True
        if error_occurred:
            return HttpResponse(t.render(c))
        else:
            return HttpResponseRedirect('/thanks')

def thanks(request):
    return HttpResponse('Thank you for signing up!')
