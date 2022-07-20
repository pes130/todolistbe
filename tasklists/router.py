from rest_framework.routers import DefaultRouter

from tasklists.views import TaskListViewSet, TaskViewSet

router = DefaultRouter()

router.register(prefix='lists', basename='lists', viewset=TaskListViewSet)
router.register(prefix='tasks', basename='tasks', viewset=TaskViewSet)