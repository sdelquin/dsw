from django.shortcuts import get_object_or_404

from .models import Event


class EventConverter:
    regex = '\d+'

    def to_python(self, event_id: str) -> Event:
        return get_object_or_404(Event, pk=event_id)

    def to_url(self, event: Event) -> str:
        return event.id
