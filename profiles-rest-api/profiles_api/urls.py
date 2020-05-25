from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views

""" 
as_view()でDjangoのビューの条件を満たす関数を作り出している
Class-based viewsをFunction-based viewsと同じ働きをするようよしなにやってくれている
・requestオブジェクトを(第一引数として)受け取る
・callableである
・responseオブジェクトを返す
"""

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
# Viewでquerysetの記述があればbasenameの設定はいらない
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('hello-view/', views.HelloAPIView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]
