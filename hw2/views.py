from django.http import HttpResponse
from django.template import loader, Context
from rot13 import rot13

def hello(request):
    t = loader.get_template('page.html')
    if request.method == "GET":
        c = Context({})
        return HttpResponse(t.render(c))
    elif request.method == "POST":
        user_input = request.POST['text']
        result = rot13(user_input)
        c = Context({'content': result})
        return HttpResponse(t.render(c))