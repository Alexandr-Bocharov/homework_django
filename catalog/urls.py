from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ContactsView, ProductListView, ProductDetailView, ProductCreateView, VersionCreateView, \
    ProductUpdateView, ProductDeleteView, VersionUpdateView, MyProductListView
from django.views.decorators.cache import cache_page, never_cache
from catalog.views import CategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('my_products/', MyProductListView.as_view(), name='my_product_list'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('create/', never_cache(ProductCreateView.as_view()), name='product_create'),
    path('create_version/', VersionCreateView.as_view(), name='version_create'),
    path('edit_product/<int:pk>/', never_cache(ProductUpdateView.as_view()), name='product_edit'),
    path('delete_product/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('edit_version/<int:pk>/', VersionUpdateView.as_view(), name='version_edit'),
    path('categories/', CategoryListView.as_view(), name='category_list')
]