from django.db import models

from apps.commons.models import TimeStampedModel
from apps.actors.models import Student


class Course(TimeStampedModel):
    name = models.CharField(max_length=63)
    created_by = models.CharField(max_length=63)
    updated_by = models.CharField(max_length=63, null=True, blank=True)
    meta = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.name)


class CourseEnrolment(TimeStampedModel):
    course = models.ForeignKey(to=Course, on_delete=models.DO_NOTHING)
    student = models.ForeignKey(to=Student, on_delete=models.DO_NOTHING)
