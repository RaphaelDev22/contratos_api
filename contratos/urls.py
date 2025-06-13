from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContratoViewSet, resumo_contratos

router = DefaultRouter()
router.register(r'contratos', ContratoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('resumo/', resumo_contratos),
]
