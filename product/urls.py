from django.urls import path

from . import views


urlpatterns = [
    path("", views.ProductListView.as_view(), name="product-list"),
    path("<int:pk>/", views.ProductDetailView.as_view(), name="product-detail"),
    path("brands/", views.BrandListView.as_view(), name="brand-list"),
    path("brands/<int:pk>/", views.BrandDetailView.as_view(), name="brand-detail"),
    path("categories/", views.CategoryListView.as_view(), name="category-list"),
    path("categories/<int:pk>/", views.CategoryDetailView.as_view(), name="category-detail"),
]
