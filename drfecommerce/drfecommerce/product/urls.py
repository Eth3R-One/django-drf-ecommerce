from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter
from . import views
# from drfecommerce.product import views

# router = DefaultRouter()
# router.register(r"category", views.CategoryViewSet)
# router.register(r"product", views.ProductViewSet)

urlpatterns = [
   path("", views.test, name="test")
]