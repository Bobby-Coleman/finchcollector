from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.FinchList.as_view(), name='finches_index'),
    path('finch/<int:finch_id>', views.finches_detail, name='finches_detail'),
]


