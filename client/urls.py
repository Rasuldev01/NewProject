from django.urls import path
from .views import CategoryApiView, CategoryFilter, ProductModelViewset, ProductUpdate, ProductFilter
from django.conf import settings
from django.conf.urls.static import static

app_name = 'client'

urlpatterns = [
    path('product/', ProductModelViewset.as_view({'get': 'list',
                                                 'post': 'create',
                                                  })),
    path('product/<int:pk>/', ProductUpdate.as_view({'put': 'update'})),
    path('product/category/<int:pk>', ProductFilter.as_view({'get': 'list'})),
    path('category/', CategoryApiView.as_view()),
    path('category/<int:pk>/', CategoryFilter.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)