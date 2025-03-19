from django.contrib import admin
from django.urls import path,include
import api
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.home,name="homepage"),
    path("api/",include("api.urls"))
]
