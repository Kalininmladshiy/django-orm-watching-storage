import django
import datetime


def get_duration(visit, current_time):
    local_visit_time = django.utils.timezone.localtime(visit.entered_at)
    duration = current_time - local_visit_time
    return duration


def is_visit_long(duration):
    visit_time_minutes = int(duration.total_seconds() // 60)
    return visit_time_minutes > 60


def get_format_duration(duration):
    duration_hours = int(duration.total_seconds() // 3600)
    duration_minutes = int((duration.total_seconds() % 3600) // 60)
    return f'{duration_hours} hours : {duration_minutes} minutes'
