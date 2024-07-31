# djangoproj/reactapp/urls.py
from django.urls import path
from . import views
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('top-gross-movies/<int:year>/', views.top_gross_movies, name='top_gross_movies'),
    path('top-voted-movies/', views.top_voted_movies, name='top_voted_movies'),
    path('top-rated-movies/<int:year>/', views.top_rated_movies, name='top_rated_movies'),
]
