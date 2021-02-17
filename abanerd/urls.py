# myapi/urls.py
from django.urls import include, path
from rest_framework import routers, urls
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)
from .views import ProvidersFilterView, MaxPriceView

router = routers.DefaultRouter()
router.register(r'providers', views.ProviderViewSet)
router.register(r'ceus', views.CEUCreditViewSet)
router.register(r'images', views.CEUImageFileViewSet)
router.register(r'ceu-media-types', views.CEUMediaTypeViewSet)
router.register(r'ceu-credit-types', views.CEUCreditTypeViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api/provider/filter/', ProvidersFilterView.as_view()),
    path('api/max/price/', MaxPriceView.as_view()),
    path('api/inject/data/', views.InjectDataView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
