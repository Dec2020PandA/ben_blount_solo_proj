from django.db import models
# Create your models here.


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.owner.id, filename)


class File(models.Model):
    location = models.FileField(upload_to=user_directory_path)
    name = models.CharField(max_length=45)
    code = models.CharField(max_length=16)
    owner = models.ForeignKey(
        'log_reg.User', related_name="files", on_delete=models.CASCADE)
    price = models.IntegerField()
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Client(models.Model):
    name = models.CharField(max_length=45)
    email = models.EmailField()
    owner = models.ForeignKey('log_reg.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
