from traceback import print_exc

from django.contrib.auth import logout
from django.http.response import HttpResponse
from django.shortcuts import render


def login_view(httpRequest):
    response = HttpResponse()
    return response


def index(request):
    user = {}
    if request.user.is_authenticated():
        user.update({"name": request.user.get_full_name()})
        user.update({"email": request.user.email})
    else:
        user.update({"name": "Guest"})
        user.update({"email": ""})
    return render(request=request, template_name="web/index.html", context=user)


def user_logout(request):
    try:
        logout(request)
    except:
        print_exc()
    return render(request, "web/index.html", {})
