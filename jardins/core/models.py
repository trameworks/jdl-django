# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField

# ABOUT
class AboutSection(models.Model):
    title = models.CharField("Título da seção", max_length=50, blank=False)
    subtitle = models.CharField("Subtítulo da seção", max_length=100, blank=False)
    resume = RichTextField("Texto descritivo", blank=True)
    image = models.ImageField("Imagem ou Logo", upload_to='images/about/', blank=False)
    active = models.BooleanField("Página ativa?", blank=True, default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name= "Seção 'Sobre'"
        verbose_name_plural = "Seções 'Sobre'"

    def __str__(self):
        if self.title:
            return self.title
        return "Title isn't available"

    def save(self, *args, **kwargs):
        if self.active:
            try:
                temp = AboutSection.objects.get(active=True)
                if self != temp:
                    temp.active = False
                    temp.save()
            except AboutSection.DoesNotExist:
                pass

        return super(AboutSection, self).save(*args, **kwargs)

# SPEAKER
class SpeakerSection(models.Model):
    title = models.CharField("Título", max_length=50, blank=False)
    subtitle = models.CharField("Subtítulo", max_length=100, blank=False)
    active = models.BooleanField("Página ativa?", blank=True, default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Seção de 'Autor'"
        verbose_name_plural = "Seções de 'Autores'"

    def __str__(self):
        if self.title:
            return self.title
        return "Title isn't available"

    def save(self, *args, **kwargs):
        if self.active:
            try:
                temp = SpeakerSection.objects.get(active=True)
                if self != temp:
                    temp.active = False
                    temp.save()
            except SpeakerSection.DoesNotExist:
                pass

        return super(SpeakerSection, self).save(*args, **kwargs)

class Speaker(models.Model):
    title = models.CharField("Nome", max_length=50, blank=False)
    subtitle = models.CharField("Sub-título", max_length=50, blank=True)
    facebook = models.URLField("Facebook URL", blank=True)
    instagram = models.URLField("Instagram URL", blank=True)
    image = models.ImageField("Avatar ou Foto", upload_to='images/speakers/', blank=False)
    speaker_section = models.ForeignKey(SpeakerSection, on_delete=models.PROTECT, verbose_name="Seção relacionada", related_name="speaker_set")

    def __unicode__(self):
        return self.title

    def get_next(self):
        next = Speaker.objects.filter(id__gt=self.id)
        if next:
          return next.first()
        return False

    def get_prev(self):
        prev = Speaker.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
          return prev.first()
        return False

    def __str__(self):
        if self.title:
            return self.title

        return "Title isn't available"

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

# SCHEDULE
class ScheduleSection(models.Model):
    title = models.CharField("Título", max_length=50, blank=False)
    subtitle = models.CharField("Subtítulo", max_length=100, blank=False)
    active = models.BooleanField("Página ativa?", blank=True, default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Seção de 'Agenda'"
        verbose_name_plural = "Seções de 'Agendas'"

    def __str__(self):
        if self.title:
            return self.title
        return "Title isn't available"

    def save(self, *args, **kwargs):
        if self.active:
            try:
                temp = ScheduleSection.objects.get(active=True)
                if self != temp:
                    temp.active = False
                    temp.save()
            except ScheduleSection.DoesNotExist:
                pass

        return super(ScheduleSection, self).save(*args, **kwargs)

class EventTag(models.Model):
    tag_name = models.CharField("Nome da categoria", max_length=50, blank=False)
    agenda = models.CharField("Datas do evento", max_length=50, blank=True)
    anchor = models.CharField("Link interno", max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        if self.tag_name:
            return self.tag_name

        return "Title isn't available"

class Event(models.Model):
    title = models.CharField("Título do evento", max_length=255, blank=False)
    time = models.CharField("Data e Hora", max_length=255, blank=False)
    speakers = models.ManyToManyField(Speaker, related_name='speaker_event_set', verbose_name="Lista de autores", blank=True)
    resume = RichTextField("Descrição da Atividade", blank=True)
    local = models.CharField("Local do evento", max_length=255, blank=False)
    tags = models.ManyToManyField(EventTag, related_name='event_set', verbose_name="Lista de tags", blank=True)
    schedule_section = models.ForeignKey(ScheduleSection, on_delete=models.PROTECT, verbose_name="Seção relacionada", related_name="schedule_set")
    label = models.CharField("ID Panel Heading", max_length=50, blank=True)
    collapse = models.CharField("Link interno", max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        if self.title:
            return self.title

        return "Title isn't available"

    def get_next(self):
        next = Event.objects.filter(id__gt=self.id)
        if next:
            return next.first()
        return False

    def get_prev(self):
        prev = Event.objects.filter(id__lt=self.id)
        if prev:
            return prev.first()
        return False
