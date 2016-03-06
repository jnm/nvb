"""nvb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers
from byke import views

router = routers.DefaultRouter()
router.register(r'bikes', views.BikeViewSet)
router.register(r'youths', views.YouthViewSet)
router.register(r'adults', views.AdultViewSet)
router.register(r'stands', views.StandViewSet)
router.register(r'skill_categories', views.SkillCategoryViewSet)
router.register(r'skills', views.SkillViewSet)
router.register(r'parts', views.PartViewSet)
router.register(r'shop_sessions', views.ShopSessionViewSet)
router.register(r'activities', views.ActivityViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
