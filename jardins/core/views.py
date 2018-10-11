from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import edit, base
from django.views.generic.detail import DetailView
from django.http import JsonResponse
import itertools
import operator

from .forms import RegisterWorkshop

from .models import AboutSection, SpeakerSection, ScheduleSection, Event, EventTag


class HomeView(base.TemplateView):
    template_name = 'core/index.html'


    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        about_section = None
        speaker_section = None
        speakers = None
        schedule_section = None
        events = None
        tags = None

        try:
            about_section = AboutSection.objects.get(active=True)
        except AboutSection.DoesNotExist:
            about_section = None

        try:
            speaker_section = SpeakerSection.objects.get(active=True)
            speakers_id_list = [1]
            speakers = speaker_section.speaker_set.all().exclude(id__in=[40])
        except SpeakerSection.DoesNotExist:
            speaker_section = None
            speakers = None

        try:
            schedule_section = ScheduleSection.objects.get(active=True)
            tags = EventTag.objects.all()
            events = Event.objects.all().order_by('created_at')
        except ScheduleSection.DoesNotExist:
            schedule_section = None
            events = None
            tags = None

        context.update({
        'about_section': about_section
        , 'speaker_section': speaker_section
        , 'speakers': speakers
        , 'schedule_section': schedule_section
        , 'events': events
        , 'tags': tags
        , 'register_workshop': RegisterWorkshop()
        })

        return context

def register_workshop(request):
    if request.POST and request.is_ajax():
        form = RegisterWorkshop(request.POST)
        data = {}
        print(form.errors)
        if form.is_valid():
            form.send_email()
            data['success'] = 'success'
            return JsonResponse(data)
        else:
            data['error'] = 'error'
            return JsonResponse(data)
    else:
        return HttpResponseRedirect("/")
