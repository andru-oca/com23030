from django.contrib import admin
from django.urls import path

from .views import Vinoteca

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Vinoteca.as_view(), name="landing_page")
]
