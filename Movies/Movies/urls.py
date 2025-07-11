"""
URL configuration for Movies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from Setup import views, feeds
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing_page, name='landing_page'),
    path('home/', views.landing_page, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('homepage/', views.home_page, name='homepage'),
    path('commits/', views.commit_list, name='commit_list'),
    path('rss/', feeds.LatestCommitsFeed(), name='rss_feed'),
    path('<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('search/', views.search_results, name='search'),
    path('h/', views.home, name="h"),
    path('search_by_year/', views.search_by_year, name='search_by_year'),
    path('random_movie/', views.random_movie, name='random_movie'),
    path('random_movie_results/', views.random_movie_results, name='random_movie_results'),
    path('search_by_year_results/', views.search_by_year_results, name='search_by_year_results'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)