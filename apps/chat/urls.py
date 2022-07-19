from rest_framework.routers import DefaultRouter
from .views import GenericFileUploadView, MessageView, ReadMultipleMessages
from django.urls import path, include

router = DefaultRouter(trailing_slash=False)

app_name = 'chat'
 
router.register("file-upload", GenericFileUploadView)
router.register("message", MessageView)

urlpatterns = [
    path("", include(router.urls)),
    path("read-messages", ReadMultipleMessages.as_view()),
]