from django.urls import path
from . import views

app_name = 'products_microservice'

urlpatterns = [
    path('products/', views.HotProductsView.as_view(), name='hot-products'),
    path('product/<int:pk>/', views.HotProductsDetailView.as_view(), name='hot-products-detail'),
    path('product-variant/<int:pk>/', views.ProductsVariantView.as_view(), name='product-variant'),
    path('category/<int:pk>/', views.CategoriesDetailView.as_view(), name='category-detail'),
    path('secure/', views.SecureView.as_view()),
    path('categories/', views.CategoriesView.as_view(), name='categories'),
    path('product/', views.ProductListView.as_view(), name='product-list'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('channel-list/', views.ChannelListView.as_view(), name='channel-list'),
    path('assessment/', views.AssessmentView.as_view(), name="assessment"),
    path('assessment/show/', views.AssessmentShowView.as_view(), name="assessment-show"),
    path('set-channel-cookie/', views.SetChannelCookieView.as_view(), name="set-channel-cookie"),
    path('get-channel-cookie/', views.GetChannelCookieView.as_view(), name="get-current-channel-cookie"),
    path('search-products/', views.SearchProductView.as_view(), name='search-products'),
]
