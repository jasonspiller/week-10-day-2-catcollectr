"""Main App URLs."""
from django.urls import path
from main_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:cat_id>/', views.show, name='show')
]
