from rest_framework import routers
from .api import UnilinkerUserViewset

router = routers.DefaultRouter()
router.register('api/user', UnilinkerUserViewset, 'unilinker_user')

urlpatterns = router.urls
