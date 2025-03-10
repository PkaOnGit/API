from django.urls import path
from . import views

#api/products
urlpatterns = [
    path('', views.product_mixin_view),
    path('<int:pk>/update/', views.product_update_view, name='product-edit'),
    path('<int:pk>/delete/', views.product_delete_view),
    path('<int:pk>/', views.product_detail_view, name='product-detail')
]