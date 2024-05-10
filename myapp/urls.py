from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('hello/<int:age>', views.hello),
    path('info/<str:username>,<int:age>', views.info)
]
