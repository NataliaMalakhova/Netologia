from django.db import models
from django.core.exceptions import ValidationError

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='articles/', blank=True, null=True)
    tags = models.ManyToManyField(Tag, through='Scope', related_name='articles')

    def __str__(self):
        return self.title

class Scope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    is_main = models.BooleanField(default=False)

    class Meta:
        unique_together = ['article', 'is_main']

    def clean(self):
        if self.is_main:
            if Scope.objects.filter(article=self.article, is_main=True).exclude(pk=self.pk).exists():
                raise ValidationError('Only one main tag is allowed per article.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.article} - {self.tag}'
