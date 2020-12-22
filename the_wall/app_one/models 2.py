from django.db import models
import re
import datetime

email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserValidator(models.Manager):    
    def validate(self, form_data):
        errors = {}
        if len(form_data['first_name']) < 2:
            errors['first_name'] = 'First name must be at least 2 characters'
        if len(form_data['last_name']) < 2:
            errors['last_name'] = 'Last name must be at least 2 characters'
        if not email_regex.match(form_data['email']):
            errors['email'] = 'Invalid email'
        if len(form_data['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters'
        if form_data['password'] != form_data['conf_password']:
            errors['password'] = 'Passwords do not match'
        if len(User.objects.filter(email=form_data['email'])) > 0:
            errors['email'] = 'Email already registered'
        
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=250)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserValidator()

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

class Post(models.Model):
    content = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='liked_posts')
    dislikes = models.ManyToManyField(User, related_name='disliked_posts')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def time(self):
        time = self.created_at.strftime("%d/%m/%y %-I:%M%p")
        return time

    @property
    def compare_time(self):
        now = datetime.datetime.now(datetime.timezone.utc)
        difference = now - self.created_at
        diff_minutes = difference.total_seconds() / 60
        return diff_minutes

class Comment(models.Model):
    content = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name='user_comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='post_comments', on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='liked_comments')
    dislikes = models.ManyToManyField(User, related_name='disliked_comments')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def time(self):
        time = self.created_at.strftime("%d/%m/%y %-I:%M%p")
        return time
    
    @property
    def compare_time(self):
        now = datetime.datetime.now(datetime.timezone.utc)
        difference = now - self.created_at
        diff_minutes = difference.total_seconds() / 60
        return diff_minutes