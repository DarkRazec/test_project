from companies.urls import router
from products.apps import ProductsConfig
from products.views import ProductsViewSet

app_name = ProductsConfig.name

router.register(r'products', ProductsViewSet, basename='products')

urlpatterns = router.urls
