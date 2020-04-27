from django.urls import path

from post.views import generate, modify


urlpatterns = [
    path('generate/', generate, name='post-generate'),
    path('modify/', modify, name='post-modify'),
]
