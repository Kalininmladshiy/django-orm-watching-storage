from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404
import django
import datetime


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard__passcode=passcode)
    this_passcard_visits = [
        {
            'entered_at': django.utils.timezone.localtime(visit.entered_at),
            'duration': get_format_duration(visit),
            'is_strange': is_visit_long(visit),
        }
        for visit in visits
    ]
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)


def get_duration(visit):
    local_leave_time = django.utils.timezone.localtime(visit.leaved_at)
    local_visit_time = django.utils.timezone.localtime(visit.entered_at)
    duration = local_leave_time - local_visit_time
    return duration


def is_visit_long(visit):
    visit_time_minutes = int(get_duration(visit).total_seconds() // 60)
    return visit_time_minutes > 60


def get_format_duration(visit):
    duration_hours = int(get_duration(visit).total_seconds() // 3600)
    duration_minutes = int((get_duration(visit).total_seconds() % 3600) // 60)
    return f'{duration_hours} hours : {duration_minutes} minutes'
