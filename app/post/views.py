import random

from django.http import JsonResponse

from post.models import Post


def generate(request):
    post_obj = Post.objects.create(
        title=f'Awesome title {random.random()}',
        content=f'Great content: {random.random()}'
    )

    return JsonResponse({
        'post_id': post_obj.id
    })


def modify(request):
    raise Exception('Oh No! Something bad happened!')
