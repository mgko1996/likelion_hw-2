from django.urls import path
from .views import first, second, third


urlpatterns = [
    path('first/', first, name = "first"),
    path('second/', second, name = "second"),
    path('third/', third, name = "third"),
]