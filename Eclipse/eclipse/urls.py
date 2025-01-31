#imports django
from django.urls import path

#views import
from .views import Index

#urls
urlpatterns = [
    path('',Index.as_view(), name="index"),
]
