from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from reminders.views import ReminderViewSet

router = DefaultRouter()
router.register(r'reminders', ReminderViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
