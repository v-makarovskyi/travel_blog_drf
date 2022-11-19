
from django.conf import settings
from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey



class Category(MPTTModel):

    class Meta: 
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    title = models.CharField('категория', max_length=100)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug = models.SlugField(max_length=100)
    image = models.ImageField('изображение', upload_to='category_images/', blank=True)
    description = models.TextField('краткое описание', max_length=700, blank=True)

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self) -> str:
        return self.title


class Tag(models.Model):

    class Meta: 
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    title = models.CharField('тег', max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self) -> str:
        return self.title


class Post(models.Model):

    class Meta: 
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='posts', on_delete=models.SET_NULL, null=True, verbose_name='автор')
    category = models.ForeignKey(Category, related_name='posts',
                                 on_delete=models.SET_NULL, null=True, verbose_name='категория')
    title = models.CharField('заголовок', max_length=150)
    image = models.ImageField(upload_to='articles/')
    text = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='post')
    slug = models.SlugField(max_length=150, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('post:post_single', kwargs={'slug': 'self.category.slug', 'post_slug': 'self.slug'})
    
    def get_comments(self):
        return self.comments.all()
    
class Comment(models.Model):

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['created_at']

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.CASCADE,)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField('текст', max_length=500)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.owner} - {self.text[:10]}'

