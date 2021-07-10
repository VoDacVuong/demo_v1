from django.urls import path
from . import views
urlpatterns = [
    path("", views.ListUser),
    path("<int:key>/", views.UserDetail),
    path("Update/<int:key>/", views.UpdateUser),
    path("CreateUser/", views.CreateUser)
]
