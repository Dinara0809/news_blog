from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    photo = models.ImageField(upload_to='photos')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)


    def get_absolute_url(self):
        return reverse('views_new', kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name = 'Новости'
        ordering = ['-create_at']


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

        class Meta:
            verbose_name = 'Котегория'
            verbose_name_plural = 'Котегории'
            ordering = ['title']
