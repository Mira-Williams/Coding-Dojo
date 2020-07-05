from django.db import models
import re

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