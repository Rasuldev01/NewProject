from django.urls import path
from .views import CategoryApiView, ProductApiView, CategoryFilter
from django.conf import settings
from django.conf.urls.static import static

app_name = 'client'

urlpatterns = [
    path('category/', CategoryApiView.as_view()),
    path('product/', ProductApiView.as_view()),
    path('category/<str:name>/', CategoryFilter.as_view())
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)