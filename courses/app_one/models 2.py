from django.db import models

class Validator(models.Manager):
    def comment_validate(self, data):
        errors = {}
        if len(data['comm_content']) < 5:
            errors['comm_content'] = 'Comment must be at least 5 characters'
        return errors

    def course_validate(self, data):
        errors = {}
        if len(data['name']) < 5:
            errors['name'] = 'Name must be at least 5 characters'
        if len(data['desc_content']) < 15:
            errors['desc_content'] = 'Description must be at least 15 characters'
        return errors


class Description(models.Model):
    desc_content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.OneToOneField(Description, related_name='course', null=True, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = Validator()


class Comment(models.Model):
    comm_content = models.CharField(max_length=255)
    course = models.ForeignKey(Course, related_name='comments', null=True, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = Validator()
