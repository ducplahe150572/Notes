from django.contrib import admin
from django.urls import path
from .views import ExView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ex/', ExView.as_view()),
]
