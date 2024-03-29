from django.db import models

# Create your models here.
from django.utils import timezone


class Comment(models.Model):
    STATUS_CHOICE = [
        (0, '不通过'),
        (1, '通过')
    ]
    name = models.CharField('名字', max_length=50)
    email = models.EmailField('邮箱')
    url = models.URLField('网址', blank=True)
    text = models.TextField('内容')
    created_at = models.DateTimeField('创建时间', default=timezone.now())
    status = models.IntegerField('审核状态', default=0, choices=STATUS_CHOICE)
    post = models.ForeignKey('blog.Post', verbose_name='文章', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        ordering = ['-created_at']

    def __str__(self):
        return  '{}: {}'.format(self.name, self.text[:20])
