from __future__ import unicode_literals
import re
from django.db import models
import time
from datetime import date, datetime
import bcrypt


# Create your models here.


class UserManager(models.Manager):

    def validate(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        dob = datetime.strptime(postData['dob'], '%Y-%m-%d')
        age = (datetime.now() - dob).days/365
        if age < 16:
            errors['dob'] = 'Must be at least 13 years old to register'
        if len(postData['first_name']) < 2:
            errors['first_name'] = 'First Name must be at least 2 characters'
        if len(postData['last_name']) < 2:
            errors['last_name'] = 'Last Name must be at least 2 characters'
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Invalid Email Address'
        email_check = self.filter(email=postData['email'])
        if email_check:
            errors['email'] = "Email already in use"
        if len(postData['pw']) < 8:
            errors['pw'] = 'Password must be at least 8 characters'
        if postData['pw'] != postData['pw_conf']:
            errors['pw'] = 'Passwords do not match'
        if dob > datetime.today():
            errors['dob'] = "Birthdate must be in the past"

        return errors

    def authenticate(self, email, password):
        users = self.filter(email=email)
        if not users:
            return False

        user = users[0]
        return bcrypt.checkpw(password.encode(), user.password.encode())

    def register(self, postData):
        pw = bcrypt.hashpw(postData['pw'].encode(),
                           bcrypt.gensalt()).decode()
        return self.create(
            first_name=postData['first_name'],
            last_name=postData['last_name'],
            company_name=postData['company'],
            email=postData['email'],
            dob=postData['dob'],
            password=pw,
        )


class User(models.Model):
    company_name = models.CharField(max_length=45)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=60)
    dob = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
