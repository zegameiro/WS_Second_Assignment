"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import include, path
from f1App import views, inference_rules

urlpatterns = [
    path("__reload__/", include("django_browser_reload.urls")),
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    # ========Races========
    path("races", views.races, name="races"),
    path("races/new",views.add_race,name="add_race"),
    path('races/<str:name>', views.race_year, name='race_year'),
    path("races/id/<int:id>",views.race_profile, name='race_profile'),
    path("races/delete/",views.race_delete, name="delete_race"),
    # ========Drivers======
    path('drivers', views.drivers, name='drivers'),
    path('drivers/<int:id>', views.driver_profile, name='driverProfile'),
    # ========Constructors========
    path('constructors',views.constructors, name="constructors"),
    # ========Seasons=============
    path('seasons',views.seasons,name="seasons"),
    path('seasons/<int:year>', views.season_profile, name="seasonsProfile"),
    path('seasons/add',views.add_season,name="add_season"),
    path('seasons/delete/<int:year>',views.delete_season,name="delete_season")
]

inference_rules.apply_inference_rules()