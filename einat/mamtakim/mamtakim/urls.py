
from django.contrib import admin
from django.urls import path, include
from mamtakim_store import views #adding my mamtakim from views.py

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('api.urls')), #view for djangorestframework
    path('restframework', include('api.urls')), #view for djangorestframework
    path('mamtakim', views.home, name='home'),
    path('mamtakim_index', views.index, name='index'),
    path('mamtakim/<int:mamtak_id>/', views.mamtak_detail,  name='mamtak_id')
]
