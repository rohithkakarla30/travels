from django.urls import path
from .views import hello, AddUserPackage
urlpatterns=[
    path('',hello),
    path('add/<int:package>/',AddUserPackage.as_view(),name='AddUserPackage')
]