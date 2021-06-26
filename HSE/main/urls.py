from django.urls import path
from .views import *

app_name = "main"

urlpatterns = [
    path("", showMain,name="showMain"),
    path("components/", componentsMain, name='componentsMain'),
]