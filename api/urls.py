from django.urls import path
from .views import PublicApiView, ProtectedApiView, RegisterView

urlpatterns = [
    path('public/', PublicApiView.as_view(), name='public-api'),
    path('protected/', ProtectedApiView.as_view(), name='protected-api'),
    path('register/', RegisterView.as_view(), name='register'),
] 