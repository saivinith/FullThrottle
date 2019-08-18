from django.urls import path
from . import views

urlpatterns = [
   path('<str:word>/', views.fuzzy_search),
   path('', views.template_view)

]