import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)

"""
from django
"""


def posts_index(request):
    # author_name = request.GET.get("author", "evgesha")
    # posts = Post.objects.
    value = request.GET.get("key")
    logger.info(value)
    return HttpResponse("Posts index view")

"""
def posts_index(request):
    posts = Post.ogjects.all()
    return HttpResponse([", ".join(x.slug for x in posts)])
"""