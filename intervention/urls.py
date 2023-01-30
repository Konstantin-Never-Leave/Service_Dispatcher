from django.contrib import admin
from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', intervention),
    path('othershit/<int:shit>/', othershit),
    path('othershit/', othershit),
    path('toomuch/', toomuch),
    re_path(r'^catofshit/(?P<number>[0-9]{3})/', numbershit)

]
