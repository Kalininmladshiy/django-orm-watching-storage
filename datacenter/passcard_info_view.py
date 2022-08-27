from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from datacenter.utils import get_format_duration, get_duration, is_visit_long
import django
import datetime


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = [
        {
            'entered_at': django.utils.timezone.localtime(visit.entered_at),
            'duration': get_format_duration(get_duration(
                visit,
                current_time=django.utils.timezone.localtime(visit.leaved_at),
                )
                                            ),
            'is_strange': is_visit_long(get_duration(
                visit,
                current_time=django.utils.timezone.localtime(visit.leaved_at),
                )
                                        ),
        }
        for visit in visits
    ]
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
