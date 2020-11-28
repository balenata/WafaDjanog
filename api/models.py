from django.db import models
from django.contrib.auth.models import User

# nawy columny table abe snake case be test_test not testTest
class Admin(User):
    created_at = models.DateTimeField(auto_now_add=True)


class AboutUs(models.Model):
    name = models.CharField(max_length=30)
    description= models.TextField()
    phone_number = models.CharField(max_length=20)
    picture = models.ImageField()

    def __str__(self):
        return self.name


class AboutUslink(models.Model):
    link = models.CharField(max_length=254)
    about_us = models.ForeignKey(AboutUs, related_name='about_us_links', on_delete=models.CASCADE,null=True)
    link_icon_image = models.ImageField(null=True)


class Blog(models.Model):
    title = models.CharField(max_length=30,null=True)
    description= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_visible = models.BooleanField(default=True) # ba by default True be

    def __str__(self):
        return self.title


class BlogLink(models.Model):
    blog = models.ForeignKey(Blog, related_name='blog_links' ,on_delete=models.CASCADE)
    link = models.CharField(max_length=254)

class BlogImage(models.Model):
    picture = models.ImageField(null=True)
    blog = models.ForeignKey(Blog,related_name='blog_images', on_delete=models.CASCADE)


class BlogVideo(models.Model):
    video = models.CharField(max_length=254,null=True)
    blog = models.ForeignKey(Blog,related_name='blog_videos', on_delete=models.CASCADE)


class Quote(models.Model):
    quoter = models.CharField(max_length=25)
    # picture = models.ImageField()
    quote = models.CharField(max_length=200)
    is_visible = models.BooleanField(default=True) # ba by default True be

    def __str__(self):
        return self.quoter

class  FieldWeWorkIn(models.Model):
    title = models.CharField(max_length=60)
    is_visible = models.BooleanField(default=True) # ba by default True be

    def __str__(self):
        return self.title

class SlideShow(models.Model):
    picture = models.ImageField()
    title = models.CharField(max_length=30)
    description= models.TextField()
    is_visible = models.BooleanField(default=True) # ba by default True be

    def __str__(self):
        return self.description


class Video(models.Model):
    video = models.CharField(max_length=254)
    is_visible = models.BooleanField(default=True) # ba by default True be

    def __str__(self):
        return self.video


class Category(models.Model):
    name = models.CharField(max_length=34) # ba by default True be



class  Ebook(models.Model):
    picture = models.ImageField()
    book_name = models.CharField(max_length=50)
    ebook_file = models.FileField(upload_to='ebooks')
    is_visible = models.BooleanField(default=True) # ba by default True be
    category = models.ForeignKey(Category, related_name='ebooks', on_delete=models.CASCADE)

class Discount(models.Model):
    field_name = models.CharField(max_length=20)
    amount_discount = models.CharField(max_length=10)
    description= models.TextField(null=True)
    
