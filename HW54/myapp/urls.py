from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from .views import SecureView

urlpatterns = [
    path('', obtain_jwt_token, name='token-obtain'),
    path('api-token-refresh/', refresh_jwt_token, name='token-refresh'),
    path('secure/', SecureView.as_view(), name='secure-view'),
]