from django.forms.models import inlineformset_factory

from .models import Author, Book

AuthorBooksFormset = inlineformset_factory(Author, Book, fields=('title',))