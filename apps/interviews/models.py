from django.db import models

from InterviewManager.utils import TimeStampedModel
from apps.actors.models import Interviewer, Student


class Interview(TimeStampedModel):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    student = models.ForeignKey(to=Student, on_delete=models.DO_NOTHING)
    interviewer = models.ForeignKey(to=Interviewer, on_delete=models.DO_NOTHING)
    is_completed = models.BooleanField(default=False, blank=True)  # We can have a status here, instead of bool
    grade = models.SmallIntegerField(null=True, blank=True)
    feedback = models.TextField(null=True, blank=True)


class InterviewerAvailability(TimeStampedModel):
    """
    Data can be archived periodically, considering past slot availability is not of a concern
    """
    interviewer = models.ForeignKey(to=Interviewer, on_delete=models.DO_NOTHING)
    slot_start_time = models.DateTimeField()
    slot_end_time = models.DateTimeField()
