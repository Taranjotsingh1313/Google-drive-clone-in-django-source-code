from django.urls import path
from .import views
urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.Login, name="login"),
    path("signup/",views.SignUp,name="signup"),
    path("folder/<int:folderid>/",views.folder, name="folder"),
    path("addFolder/", views.addfolder, name="addfolder"),
    path("logout/", views.Logout, name="logout"),
]
