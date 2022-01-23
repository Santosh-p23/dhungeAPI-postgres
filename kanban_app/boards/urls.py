from django.urls import path
from rest_framework import routers
from .api import BoardViewSet, ColumnViewSet, TaskViewSet

router = routers.DefaultRouter()
router.register('api/boards',BoardViewSet, 'boards')
router.register('api/columns',ColumnViewSet, 'columns')
router.register('api/tasks',TaskViewSet, 'tasks')

urlpatterns = router.urls
