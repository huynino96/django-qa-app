from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# Question Model
class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    detail = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# Answer Model
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    detail = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# Comment Model
class Comment(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comment_user')
    create_time = models.DateTimeField(auto_now_add=True)


# Upvoet Model
class Upvote(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='upvote_user')


# Downvote Model
class Downvote(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='downvote_user')
