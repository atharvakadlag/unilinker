from main.api import LinkViewSet, ProfileViewSet, UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register('api/user', UserViewSet, 'user')
router.register('api/profile', ProfileViewSet, 'profile')
router.register('api/link', LinkViewSet, 'link')

urlpatterns = router.urls
