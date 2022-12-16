from rest_framework import routers
from .api import UsuarioViewSet

router=routers.DefaultRouter()

router.register('api/API1', UsuarioViewSet, 'usuarios')

urlpatterns=router.urls
