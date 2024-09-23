from rest_framework.routers import DefaultRouter

from companies.apps import CompaniesConfig
from companies.views import CompaniesViewSet

app_name = CompaniesConfig.name

router = DefaultRouter()
router.register(r'companies', CompaniesViewSet, basename='companies')

urlpatterns = router.urls