from django.views.generic import ListView
from .models import Posts


class PostsList(ListView):
    model = Posts
    ordering = 'name_post'
    template_name = 'posts.html'
    context_object_name = 'posts'