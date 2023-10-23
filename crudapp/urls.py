from django.urls import path
from .views import sport

urlpatterns = [
    path('sport-items', sport.as_view()),
    path('sport-items/<int:id>/', sport.as_view())
]