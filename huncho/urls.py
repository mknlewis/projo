from django.urls import path
from . import views

app_name = 'huncho'

urlpatterns = [

    path('',views.memberListview.as_view(),name='index'),
    path('add-member', views.memberCreateView.as_view(), name='add-member'),
    path('<int:pk>/update',views.memberUpdateView.as_view(),name='update-member'),
    path('<int:pk>/delete',views.memberDeleteView.as_view(),name='delete-member'),



]