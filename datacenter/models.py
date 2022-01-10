from django.db import models
from django.utils.timezone import localtime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


def format_duration(duration):
    hours = int(duration.total_seconds() // 3600)
    minutes = (duration.seconds // 60) % 60
    return f'{hours}ч {minutes}мин'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved='leaved at ' + str(self.leaved_at) if self.leaved_at else 'not leaved'
        )

    def get_duration(self):
        if not self.leaved_at:
            return localtime() - localtime(self.entered_at)
        return localtime(self.leaved_at) - localtime(self.entered_at)

    def is_visit_long(self, minutes=60):
        visit_duration_minutes = self.get_duration().seconds // 60
        return visit_duration_minutes > minutes
