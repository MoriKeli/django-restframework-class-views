from django.urls import path
from rest_api import views

urlpatterns = [
    path('', views.ArticleGenericView.as_view()),
    path('details/<int:pk>/', views.ArticleDetails.as_view()),
    
]