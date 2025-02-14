from django.urls import path
from rango import views  

urlpatterns = [
    path('', views.index, name='index'),  # Homepage
    path('about/', views.about, name='about'),  # About page
    path('category/<slug: category_name_slug>/',views.show_category,
         name='show_category'),
]
