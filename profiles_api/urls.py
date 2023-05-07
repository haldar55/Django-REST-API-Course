from django.urls import path, include
from rest_framework.routers import DefaultRouter

from profiles_api import views


router = DefaultRouter()
router.register(r'hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register(r'profile', views.UserProfileViewSet) # no basename, since queryset assigned in views


urlpatterns = [
    path('hello-view/', views.HelloAPIView.as_view()),
    path('', include(router.urls)),
]