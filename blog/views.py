from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.


def post_list(request: HttpRequest) -> HttpResponse:
    return render(request, 'blog/post_list.html', {})
