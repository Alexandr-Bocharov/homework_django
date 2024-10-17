from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ContactsView, ProductListView, ProductDetailView, ProductCreateView, VersionCreateView, \
    ProductUpdateView, ProductDeleteView, VersionUpdateView, MyProductListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('my_products/', MyProductListView.as_view(), name='my_product_list'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('create_version/', VersionCreateView.as_view(), name='version_create'),
    path('edit_product/<int:pk>/', ProductUpdateView.as_view(), name='product_edit'),
    path('delete_product/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('edit_version/<int:pk>/', VersionUpdateView.as_view(), name='version_edit'),
]