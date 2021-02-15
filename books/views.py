from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, CreateView, DetailView, FormView)
from django.contrib import messages
from django.urls import reverse
from django.views.generic.detail import SingleObjectMixin
from django.http import HttpResponseRedirect

from .models import Author
from .forms import AuthorBooksFormset


class HomeView(TemplateView):
    template_name = 'home.html'


class AuthorListView(ListView):
    model = Author
    template_name = 'author_list.html'


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'


class AuthorCreateView(CreateView):
    model = Author
    template_name = 'author_create.html'
    fields = ['name',]

    def form_valid(self, form):

        messages.add_message(
            self.request, 
            messages.SUCCESS,
            'The author has been added'
        )

        return super().form_valid(form)

class AuthorBooksEditView(SingleObjectMixin, FormView):

    model = Author
    template_name = 'author_books_edit.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Author.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Author.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return AuthorBooksFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('books:author_detail', kwargs={'pk': self.object.pk})

    

