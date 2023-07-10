from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.entry, name="title"),
    path('search/', views.search_results, name="search_results"),
    path('create/', views.create_page, name='create_page'),
    path('edit/<str:name>', views.edit_page, name='edit_page'),
    path('random/', views.random_page, name='random_page')
]
