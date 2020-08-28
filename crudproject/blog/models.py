from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
class Memo(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
    #today = timezone.now() #새미누나 코드

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Memo,on_delete=models.CASCADE)
    body = models.CharField("내용", max_length=250)
    create_at = models.DateTimeField('작성시간', default = timezone.now)

    def __str__(self):
        return self.body
    