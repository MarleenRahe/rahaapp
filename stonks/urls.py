from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    path("adddept", views.add_dept_page, name= "adddept"),
]