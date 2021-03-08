from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from . import util
from django import forms
from django.core.exceptions import ValidationError

import random

class NewEntryForm(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(label="Content")
    
    def title_exist(self):
        #method to validate if the title already exists
        data = self.cleaned_data["title"]
        entries = str(util.list_entries()).lower()
        return str(data).lower() in entries
#            raise ValidationError(f'"{data}" entry already exists.')
#        return data

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki_title(request, title):
    content = util.get_html_entry(title)
    return render(request, "encyclopedia/wiki-entry.html", {
        "title": title,
        "content": content,
    })
def wiki_search(request):
    query = request.GET.get('q')
    content = util.get_html_entry(query)
    entries = []
    if content == None:
        all_entries = util.list_entries()
        for title in all_entries:
            if query in title:
                entries.append(title)
        return render(request, "encyclopedia/wiki-search.html", {
        "query": query,
        "entries": entries,
    })
    else:
        return render(request, "encyclopedia/wiki-entry.html", {
        "title": query,
        "content": content,
    })

def wiki_new(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid() and not form.title_exist():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("wiki-title", args=(title,)))#return HttpResponseRedirect("/wiki/" + title)
        else:
            title = form.cleaned_data["title"]
            return render(request, "encyclopedia/wiki-new.html", {
                "form": form,
                "error": f'Entry "{title}" already exists.',
            })
    return render(request, "encyclopedia/wiki-new.html", {
        "form": NewEntryForm(),
    })

def wiki_edit(request, t):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("wiki-title", args=(title,)))#return HttpResponseRedirect("/wiki/" + title)
    return render(request, "encyclopedia/wiki-edit.html", {
        "title" : t,
        "content": util.get_entry(t),
    })

def wiki_random(request):
    title = random.sample(util.list_entries(), 1)[0]
    content = util.get_html_entry(title)
    return HttpResponseRedirect(reverse("wiki-title", args=(title,)))#return HttpResponseRedirect("/wiki/" + title)