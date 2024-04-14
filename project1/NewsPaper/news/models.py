from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

# Create your models here.

class Authors(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    evaluationAuthor = models.SmallIntegerField(default=0.00)

    def update_evaluations(self):
        postEval= self.posts_set.aggregate(postRating=Sum('rating'))
        pEval=0
        pEval += postEval.get('postRating')

        commentEval=self.authorUser.comment_set.aggregate(commentRating=Sum('rating'))
        cEval=0
        cEval += commentEval.get('commentRating')

        self.evaluationAuthor = pEval*3 + cEval
        self.save()


class Category(models.Model):
    name_category = models.CharField(max_length=64, unique = True)


class Posts(models.Model):
    NEWS = "NW"
    ARTICLE = "AR"
    CATEGORY_CHOICES = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья')
    )
    name_post = models.CharField(max_length = 128)
    text_post = models.TextField()
    rating = models.SmallIntegerField(default=0.00)
    posts = models.ForeignKey(Authors, on_delete=models.CASCADE)
    content_type = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=ARTICLE)
    date_post = models.DateTimeField(auto_now_add=True)
    postCategory = models.ManyToManyField(Category, through='PostCategory')

    def like(self):
        self.rating +=1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text_post[0: 123]+'...'


class PostCategory(models.Model):
    postThrough = models.ForeignKey(Category, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Posts, on_delete=models.CASCADE)


class Comment(models.Model):
    commentPost = models.ForeignKey(Posts, on_delete=models.CASCADE)
    commentUser= models.ForeignKey(User, on_delete=models.CASCADE)
    text_comment = models.TextField()
    date_comment = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0.00)

    def like(self):
        self.rating +=1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()



