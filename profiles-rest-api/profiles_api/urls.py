from django.urls import path

from profiles_api import views

""" 
as_view()でDjangoのビューの条件を満たす関数を作り出している
Class-based viewsをFunction-based viewsと同じ働きをするようよしなにやってくれている
・requestオブジェクトを(第一引数として)受け取る
・callableである
・responseオブジェクトを返す
"""

urlpatterns=[
    path('hello-view', views.HelloAPIView.as_view()),
]