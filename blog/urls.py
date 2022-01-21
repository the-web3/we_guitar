from typing import Any, List
from django.contrib import admin
from django.urls import include, path
from blog.views import index, artcle

urlpatterns: List[Any] = [
    path(r'', index, name='index'),
    path(r'artcle', artcle, name='artcle'),
]