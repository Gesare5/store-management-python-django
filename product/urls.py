from django.urls import path

from . import views


urlpatterns = [
    path("", views.ProductListView.as_view(), name="product-list"),
    path("<int:pk>/", views.ProductDetailView.as_view(), name="product-detail"),
    # path("update/<int:pk>/", views.ProductUpdateView.as_view(), name="product-update"),
]
