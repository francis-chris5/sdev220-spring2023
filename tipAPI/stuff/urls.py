# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 18:22:51 2023

@author: franc

sdev 220 spring 2023
"""

from django.urls import path
from . import views


urlpatterns = [
    path("", views.homePage),
    path("template", views.basicTemplate),
    path("calculate", views.calculateTip),
    path("display", views.displayTip),
    path("contacts", views.simpleAPI)
    ]