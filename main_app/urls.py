from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name='finches_index'),
    path('finch/<int:pk>', views.FinchDetail.as_view(), name='finches_detail'),
    path('finch/create', views.FinchCreate.as_view(), name='finches_create'),
    path('finches/<int:pk>/update',  views.FinchUpdate.as_view(), name='finches_update'),
    path('finches/<int:pk>/',  views.FinchDelete.as_view(), name='finches_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]


