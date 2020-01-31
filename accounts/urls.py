from django.urls import path
from . import views


urlpatterns = [
    path('singup/', views.SignUoView.as_view(), name="signup"),

]