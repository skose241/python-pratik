from django.urls import path
from . import views

urlpatterns=[
    path("merhaba/",views.merhaba),
    path("liste/",views.liste),
    path("api/liste/",views.api_liste),
    path("api/liste/<int:id>/",views.api_detay),
]