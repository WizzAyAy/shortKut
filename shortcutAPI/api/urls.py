from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
