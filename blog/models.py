from django.db import models

# Create your models here.


class Tag(models.Model):
    caption = models.CharField(max_length=100)

    def __str__(self):
        return self.caption


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()

    def __str__(self):
        return self.first_name


class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.TextField(max_length=200)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(default="", null=False,
                            unique=True, editable=False)
    content = models.TextField()
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, related_name="posts", null=True)
    tags = models.ManyToManyField(Tag, verbose_name=("tags"))

    def __str__(self):
        return self.title
