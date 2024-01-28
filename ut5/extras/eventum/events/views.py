from django.shortcuts import redirect, render

from .forms import AddEventForm
from .models import Event


def list(request):
    return render(request, 'events/list.html', dict(events=Event.objects.all()))


def add(request):
    if request.method == 'GET':
        form = AddEventForm()
    else:
        form = AddEventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('events:list')
    return render(request, 'events/add.html', dict(form=form))


def detail(request, event: Event):
    return render(request, 'events/detail.html', dict(event=event))
