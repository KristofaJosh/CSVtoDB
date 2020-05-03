from django.urls import path
from .views import ZenoView, ZenoPost, ZenoUpload

urlpatterns = [
    path('all/', ZenoView.as_view()),
    path('post/', ZenoPost.as_view()),
    path('upload/', ZenoUpload.as_view()),
]
