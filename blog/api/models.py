from django.conf import settings
from django.db import models
# import cloudinary
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_delete
from cloudinary.models import CloudinaryField
from django.dispatch import receiver
# from django.contrib.auth import 

class Category(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name

class Blog(models.Model):
  title = models.CharField(max_length=100, null=False, blank=False)
  body = models.TextField(max_length=350, null=False, blank=False)
  image = CloudinaryField('images')
  date_published = models.DateTimeField(auto_now_add=True,verbose_name='date_published')
  date_updated = models.DateTimeField(auto_now_add=True, verbose_name='date_updated')
  Author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
  likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="likes")
  # CharField(max_length=50, null=False, blank=False)
  # ForeignKey(settings.AUTH_USER, on_delete=models.CASCADE)

  def __str__(self):
    return self.title


# @receiver(post_delete, sender=Blog)
# def submission_delete(sender, instance, **kwargs):
#   instance.image.delete(False)

# def pre_save_blog_post_reciever(sender, instance, *args, **kwargs):
#   if not instance.slug :
#      instance.slug = slugify(instance.author + "." + instance.title)
#   pre_save.connect(pre_save_blog_post_reciever, sender=Blog)

class Comment(models.Model):
  blog = models.ForeignKey(Blog,related_name="comments" ,on_delete=models.CASCADE)
  body = models.TextField()
  name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  date_added = models.DateTimeField(auto_now_add=True)


  def __str__(self):
    return '%s - %s' % (self.blog.title,self.name)