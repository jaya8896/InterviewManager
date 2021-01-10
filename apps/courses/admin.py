from django.contrib import admin

from apps.courses.models import Course, CourseEnrolment


class CourseAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Course._meta.fields]
    search_fields = ['name']


class CourseEnrolmentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CourseEnrolment._meta.fields]
    search_fields = ['course__name', 'student__user__first_name']


admin.site.register(Course, CourseAdmin)
admin.site.register(CourseEnrolment, CourseEnrolmentAdmin)
