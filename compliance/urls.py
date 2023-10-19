from django.urls import path

from .views import *

urlpatterns = [
    path('get_add_applications/', ApplicationView.as_view()),
    path('get_add_compliance/', ComplianceView.as_view()),

]