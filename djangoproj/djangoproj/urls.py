"""
URL configuration for djangoproj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib.staticfiles.views import serve  # Ensure this import is present
from django.views.generic import TemplateView
from reactapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('reactapp.urls')),  # Adjust this based on your app's URLs
    # Other paths as needed for your application

    # Serve the React app's index.html
    path('',views.IndexView.as_view(), name='index'),

    # Optional: Redirect other paths to the React app
    path('<path:resource>/', serve, kwargs={'path': 'build/index.html'}),
]
# Serve static and media files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)