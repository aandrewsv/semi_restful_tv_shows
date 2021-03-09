from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/new', views.new),
    path('shows/create', views.newshow),
    path('shows/<int:idn>', views.displayshow),
    path('shows/<int:idn>/edit', views.editshow),
    path('shows/<int:idn>/update', views.update),
    path('shows/<int:idn>/destroy', views.destroy),
    ]