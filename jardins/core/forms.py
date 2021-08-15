# -*- coding: utf-8 -*-
from django import forms
from django.core.mail import EmailMessage, BadHeaderError
from django.template.loader import get_template
from django.conf import settings
from ckeditor.widgets import CKEditorWidget

class RegisterWorkshop(forms.Form):
    escolas = 'Selecione uma escola'
    ifpe = 'IFPE Campus Belo Jardim'
    erem_bj = 'EREM Belo Jardim'
    erem_jm = 'EREM João Monteiro de Melo'
    esc_mg = 'Escola Professora Maria Galvão'
    esc_jvc = 'Centro de Excelência Municipal Professor José Vieira da Costa'
    esc_mbf = 'Escola Ministro Marcos de Barros Freire'
    esc_vjm = 'Escola Municipal Vereador Joaquim Medeiros'
    ete_emm = 'ETE - Edson Mororó Moura'
    esc_pgt = 'Escola Padre Giovanni Toniutti'
    esc_lll = 'Escola Municipal Luíza Leopoldina Lopes'
    esc_mta = 'Escola Municipal Manoel Teodoro De Arruda'
    esc_avm = 'Escola Municipal Professor Antenor Vieira de Melo'

    workshops = 'Selecione uma oficina'
    work_escrita = 'Escrita Criativa'
    work_declama = 'Declamação'
    work_video = 'Vídeo-Poema'

    SCHOOLS = (
    (escolas, 'Selecione uma escola'),
    # (ifpe, 'IFPE Campus Belo Jardim'),
    (erem_bj, 'EREM Belo Jardim'),
    (erem_jm, 'EREM João Monteiro de Melo'),
    # (esc_mg, 'Escola Professora Maria Galvão'),
    # (esc_jvc, 'Centro de Excelência Municipal Professor José Vieira da Costa'),
    # (esc_mbf, 'Escola Ministro Marcos de Barros Freire'),
    (esc_vjm, 'Escola Municipal Vereador Joaquim Medeiros'),
    (ete_emm, 'ETE - Edson Mororó Moura'),
    # (esc_pgt, 'Escola Padre Giovanni Toniutti'),
    # (esc_lll, 'Escola Municipal Luíza Leopoldina Lopes'),
    # (esc_mta, 'Escola Municipal Manoel Teodoro De Arruda'),
    # (esc_avm, 'Escola Municipal Professor Antenor Vieira de Melo'),
    )

    # WORKSHOPS = (
    # (workshops, 'Selecione uma oficina'),
    # (work_escrita, 'Escrita Criativa'),
    # (work_declama, 'Declamação'),
    # (work_video, 'Vídeo-Poema'),
    # )

    #BIRTH_YEAR_CHOICES = ('Ano de Nascimento', '1980', '1981', '1982','1983', '1984', '1985','1986', '1987', '1988','1989', '1990', '1991','1992', '1993', '1994','1995', '1996', '1997','1998', '1999', '2000','2001', '2002', '2003')

    name = forms.CharField(widget=forms.TextInput(attrs={"class":"controled form-control", "placeholder":"Nome Completo", "required":"required", "data-msg-required":"Por favor digite o seu nome"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"controled form-control", "placeholder":"Email", "data-msg-required":"Por favor digite o seu endereço de email"}))
    phonenumber = forms.CharField(widget=forms.TextInput(attrs={"class":"controled form-control", "placeholder":"Telefone (Whatsapp)", "required":"required", "data-msg-required":"Por favor digite o seu telefone"}))
    age = forms.CharField(widget=forms.TextInput(attrs={"class":"controled form-control", "placeholder":"Idade", "required":"required", "data-msg-required":"Por favor digite a sua idade"}))
    school = forms.ChoiceField(widget=forms.Select(attrs={"class":"controled form-control", "placeholder":"Qual a sua Escola?", "required":"required", "data-msg-required":"Por favor insira sua escola"}),choices=SCHOOLS)
    # workshop = forms.ChoiceField(widget=forms.Select(attrs={"class":"controled form-control", "placeholder":"Selecione a Oficina", "required":"required", "data-msg-required":"Por favor selecione a oficina"}),choices=WORKSHOPS)
    # message = forms.CharField(widget=CKEditorWidget(attrs={"class":"controled form-control", "placeholder":"Escreva aqui a sua poesia", "data-msg-required":"Por favor digite uma mensagem", "rows":"4"}))
    message = forms.CharField(widget=CKEditorWidget())

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        phonenumber = self.cleaned_data['phonenumber']
        age = self.cleaned_data['age']
        school = self.cleaned_data['school']
        # workshop = self.cleaned_data['workshop']
        message = self.cleaned_data['message']
        subject = "JARDINS 2021 - Inscrição"
        html_template = get_template("core/partials/email.html")
        html_message = html_template.render({
            'name': name,
            'email': email,
            'phonenumber': phonenumber,
            'age': age,
            'school': school,
            # 'workshop': workshop,
            'message': message
        })
        try:
            email = EmailMessage(subject, html_message, email, ["jardinsdaliteratura@gmail.com"])
            email.content_subtype = "html"
            email.send()
        except BadHeaderError:
            raise ValidationError
