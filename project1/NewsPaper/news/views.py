

# Create your views here.
from django.views.generic import ListView
from .models import Posts


class PostsList(ListView):
    model = Posts
    ordering = 'name_posts'
    template_name = 'posts.html'
    context_object_name = 'posts'