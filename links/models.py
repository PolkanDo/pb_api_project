from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()

CHOICES = ("PipeDrive", "ARM", "Jira", "Other")


class Link(models.Model):
    type = models.CharField(max_length=25, choices=CHOICES)
    title = models.CharField(max_length=50)
    link = models.SlugField(max_length=20)
    description = models.CharField(max_length=200)
    img = models.ImageField()
    bloc = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата публикации', auto_now_add=True
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts'
    )
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True
    )

    class Meta:
        ordering = ("-pub_date",)

    def __str__(self):
        author = self.author
        pub_date = self.pub_date
        text = self.text[:100]
        return f'Дата публикации: {pub_date}, Автор: {author}, Пост:{text}.'
