from django.contrib import admin

from apps.interviews.models import Interview, InterviewerAvailability


class InterviewAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Interview._meta.fields]
    search_fields = ['student__user__first_name']


class InterviewerAvailabilityAdmin(admin.ModelAdmin):
    list_display = [field.name for field in InterviewerAvailability._meta.fields]
    search_fields = ['interviewer__user__first_name']


admin.site.register(Interview, InterviewAdmin)
admin.site.register(InterviewerAvailability, InterviewerAvailabilityAdmin)
