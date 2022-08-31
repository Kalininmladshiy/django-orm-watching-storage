from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.utils import get_format_duration, get_duration
import django
import datetime


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = []
    params = {}
    for visit in visits:
        params['who_entered'] = visit.passcard.owner_name
        params['entered_at'] = django.utils.timezone.localtime(visit.entered_at)
        params['duration'] = get_format_duration(get_duration(visit, django.utils.timezone.localtime()))
        non_closed_visits.append(params)
        params = {}
    context = {
        'non_closed_visits': non_closed_visits,
     }
    return render(request, 'storage_information.html', context)
