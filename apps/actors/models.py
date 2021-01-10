from django.db import models

from InterviewManager.utils import TimeStampedModel

"""
- This would be better if attributes we store against Student & Interviewer 
would not have much in common and grow in future.
- In case we are sure about collecting same user data from every actor, we might just have one User table defined, have
a Role table and sort of have a UserRoleMap.

Understanding future requirements of the product might help us here.
"""


class User(TimeStampedModel):
    first_name = models.CharField(max_length=31, blank=True)
    last_name = models.CharField(max_length=31, blank=True)
    email = models.EmailField(blank=True, db_index=True)
    mobile_number = models.CharField(max_length=13, db_index=True)

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)


class Student(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.user.first_name) + ' ' + str(self.user.last_name)


class Interviewer(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.user.first_name) + ' ' + str(self.user.last_name)
