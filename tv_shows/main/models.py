from django.db import models
from datetime import datetime  


class Validator(models.Manager):
    def validate(self, data):
        errors = []
        if data['title'] == '':
            errors.append('Please enter a title')
        elif len(data['title']) < 2:
            errors.append('Title must be at least two characters')
        elif self.filter(title=data['title']):
            errors.append('Title already in use')
        if data['network'] == '':
            errors.append('Please enter a network')
        elif len(data['network']) < 3:
            errors.append('Network must be at least three characters')
        if data['description'] == '':
            errors.append('Please enter a description')
        if len(data['description']) < 10:
            errors.append('Description must be at least ten characters')
        if data['release_date'] == '':
            errors.append('Please enter a release date')
        else:
            date = datetime.strptime(data['release_date'], '%Y-%m-%d')
            if date > datetime.now():
                errors.append('Must be a past date')
        
        return errors

    def validate_update(self, data, id):
        # errors = self.validate(data)

        errors = []
        if data['title'] == '':
            errors.append('Please enter a title')
        elif len(data['title']) < 2:
            errors.append('Title must be at least two characters')
        elif self.exclude(id=id).filter(title=data['title']):
            errors.append('Title already in use')
        if data['network'] == '':
            errors.append('Please enter a network')
        elif len(data['network']) < 3:
            errors.append('Network must be at least three characters')
        if data['description'] == '':
            errors.append('Please enter a description')
        if len(data['description']) < 10:
            errors.append('Description must be at least ten characters')
        if data['release_date'] == '':
            errors.append('Please enter a release date')
        else:
            date = datetime.strptime(data['release_date'], '%Y-%m-%d')
            if date > datetime.now():
                errors.append('Must be a past date')

        if self.exclude(id=id).filter(title=data['title']):
            errors.append('Title already in use')

        return errors


class Show(models.Model):
    title = models.CharField(max_length=50)
    network = models.CharField(max_length=50)
    release_date = models.DateField()
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    now = datetime.now()

    objects = Validator()