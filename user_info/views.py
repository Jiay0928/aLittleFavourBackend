from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from util.helper import http_method_list


# Create your views here.
class UserinfoView(View):
    @http_method_list(["GET"])
    def getUserInfo(request, userid: int):
        return HttpResponse("HelloWorld")