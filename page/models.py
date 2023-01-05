from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=255, name='Заголовок')
    slug = models.SlugField(name='URL')
    content = models.TextField(max_length=255, name='Текст статьи')
    photo = models.ImageField(blank=True,upload_to='photos/%Y/%m/%d/' , name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, name='Время создания')
    time_update = models.DateTimeField(auto_now=True, name='Последнее обновление')
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title