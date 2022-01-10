from datacenter.models import Passcard
from datacenter.models import Visit, format_duration
from django.shortcuts import render


def passcard_info_view(request, passcode):
    # Программируем здесь
    passcard = Passcard.objects.get(passcode=passcode)
    passcard_visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for passcard_visit in passcard_visits:
        this_passcard_visits.append({
            'entered_at': passcard_visit.entered_at,
            'duration': format_duration(passcard_visit.get_duration()),
            'is_strange': passcard_visit.is_visit_long(),
        })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
