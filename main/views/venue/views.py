# -*- coding: utf-8 -*-
# Project: RegisVac

from django.views import generic
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import Group, User
from django.contrib.auth.mixins import LoginRequiredMixin

from main.forms.operator.forms import MyUserCreationForm, OperatorCreationForm, OperatorRemoveForm

app_name = 'main'


# 一覧画面
class VenueListView(LoginRequiredMixin, generic.ListView):
    model = User
    template_name = "main/venue/venue_list.html"
    object_list = User.objects.order_by('username')
    success_url = reverse_lazy('home')


# 登録画面
# まっさらな状態
class VenueCreateView(CreateView):
    model = User
    form_class = MyUserCreationForm
    template_name = "main/venue/venue_form.html"
    success_url = reverse_lazy('main:venue_list')


# 更新画面
class VenueUpdateView(UpdateView):
    model = User
    form_class = MyUserCreationForm
    template_name = "main/venue/venue_form.html"
    success_url = reverse_lazy('main:venue_list')