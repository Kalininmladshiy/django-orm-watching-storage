import django
import datetime
from datacenter.models import Visit


def get_duration(visit):
    local_visit_time = django.utils.timezone.localtime(visit.entered_at)
    if visit.leaved_at:
        end_time = django.utils.timezone.localtime(visit.leaved_at)
    else:
        end_time = django.utils.timezone.localtime()
    duration = end_time - local_visit_time
    return duration


def is_visit_long(duration):
    visit_time_minutes = int(duration.total_seconds() // 60)
    return visit_time_minutes > 60


def get_format_duration(duration):
    duration_hours = int(duration.total_seconds() // 3600)
    duration_minutes = int((duration.total_seconds() % 3600) // 60)
    return f'{duration_hours} hours : {duration_minutes} minutes'
