from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
import django
import datetime


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = [
        {
            'who_entered': visit.passcard.owner_name,
            'entered_at': django.utils.timezone.localtime(visit.entered_at),
            'duration': format_duration(get_duration(visit)),
            }
        for visit in visits
    ]
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)


def get_duration(visit):
    current_time = django.utils.timezone.localtime()
    local_visit_time = django.utils.timezone.localtime(visit.entered_at)
    duration = current_time - local_visit_time
    return duration


def format_duration(duration):
    hours = int(duration.total_seconds() // 3600)
    minutes = int((duration.total_seconds() % 3600) // 60)
    return f'{hours}:{minutes}'
