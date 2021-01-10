from django.conf.urls import url

from apps.interviews.views import AvailableInterviewSlotsView

urlpatterns = [
    url(r'^slots/$', AvailableInterviewSlotsView.as_view(), name='interview_slots'),
]