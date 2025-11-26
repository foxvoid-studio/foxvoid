from django.urls import path
from . import views


urlpatterns = [
    path('', views.GameListView.as_view(), name="game_list_view"),
    path('<uuid:pk>/', views.GameDetailView.as_view(), name="game_detail_view")
]
