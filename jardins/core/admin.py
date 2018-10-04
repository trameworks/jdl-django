from django.contrib import admin

from .models import AboutSection, SpeakerSection, Speaker, ScheduleSection, Event, EventTag

class SpeakerInline(admin.TabularInline):
    model = Speaker
    max_num = 12

class SpeakerSectionAdmin(admin.ModelAdmin):
    inlines = [SpeakerInline]

class EventInline(admin.TabularInline):
    model = Event
    max_num = 12

class ScheduleSectionAdmin(admin.ModelAdmin):
    inlines = [EventInline]

admin.site.register(AboutSection)
admin.site.register(Speaker)
admin.site.register(SpeakerSection, SpeakerSectionAdmin)
admin.site.register(Event)
admin.site.register(ScheduleSection, ScheduleSectionAdmin)
admin.site.register(EventTag)
