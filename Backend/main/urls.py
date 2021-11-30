from django.urls import path
from .views import Plans


urlpatterns = [
    path('', Plans.as_view()),
]