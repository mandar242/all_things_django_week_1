from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('add/', views.addMamtak),
    path('mamtakim/<int:mamtak_id>/', views.mamtak_detail, name='mamtak_detail'),
#    path('delete/', views.deleteMamtak)
]