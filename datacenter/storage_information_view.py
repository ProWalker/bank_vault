from datacenter.models import Passcard
from datacenter.models import Visit, format_duration
from django.shortcuts import render


def storage_information_view(request):
    # Программируем здесь

    storage_visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for storage_visit in storage_visits:
        non_closed_visit = {
            'who_entered': storage_visit.passcard.owner_name,
            'entered_at': storage_visit.entered_at,
            'duration': format_duration(storage_visit.get_duration()),
        }
        non_closed_visits.append(non_closed_visit)

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
