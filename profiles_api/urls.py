from django.urls import path,include
from profiles_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# create url
router.register('helloViewSet',views.HelloViewSet,basename='helloViewSet')
router.register('profile_viewset',views.UserProfileviewSet)
urlpatterns = [
    path('hello_api', views.HelloAPI.as_view()),
    path('',include(router.urls))
]
