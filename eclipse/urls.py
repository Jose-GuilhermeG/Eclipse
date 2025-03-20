#django imports
from django.urls import re_path

#views imports
from .views import Index

urlpatterns = [
    re_path(r'^$',Index.as_view(),name="index"),
]
