from django.http import HttpResponseNotFound
from django.shortcuts import render, HttpResponse, Http404, redirect
from django.views.generic import ListView, DetailView, CreateView, FormView


def intervention(request):
    return HttpResponse('some shit')


def othershit(request, shit=0):
    return HttpResponse(f'<h1>this is an other shit </h1> '
                        f'<h2>{shit}</h2>')


def numbershit(request, number):
    if int(number) > 998:
        return redirect('/toomuch')
    return HttpResponse(f'<h1>this is a number shit </h1> '
                        f'<h2>{number}</h2>')


def not_found(request, exception):
    return HttpResponseNotFound(f'page "{request.path}/" do not exist')


def toomuch(request):
    return HttpResponse(f'it\'s realy too much')