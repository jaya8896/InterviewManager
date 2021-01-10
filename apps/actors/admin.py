from django.contrib import admin

from apps.actors.models import User, Student, Interviewer


class UserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in User._meta.fields]
    search_fields = ['first_name', 'last_name', 'email', 'mobile_number']


class StudentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Student._meta.fields]


class InterviewerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Interviewer._meta.fields]


admin.site.register(User, UserAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Interviewer, InterviewerAdmin)
