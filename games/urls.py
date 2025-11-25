from django.urls import path
from . import views


urlpatterns = [
    path('<uuid:pk>/', views.GameDetailView.as_view(), name="game_detail_view")
]
