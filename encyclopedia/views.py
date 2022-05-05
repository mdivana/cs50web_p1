from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from markdown2 import Markdown
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def converter(entry):
    html = Markdown().convert(util.get_entry(entry)) if entry else None
    return html

def entrypage(request, entry):
    html = converter(entry)
    if html is None:
        return render(request, "encyclopedia/noenrty.html", {"entrytitle": entry})
    else:
        return render(request, "encyclopedia/entrypage.html", {
            "entry": html,
            "entrytitle": entry,
        })

def search(request):
    query = request.GET.get('q','')
    entries = util.list_entries()
    if (util.get_entry(query) is not None):
        return HttpResponseRedirect(reverse("entry", kwargs={'entry': query}))
    else:
        entry_list = []
        for entry in entries:
            if query.lower() in entry.lower():
                entry_list.append(entry)
        return render(request, "encyclopedia/index.html", {
            "entries": entry_list,
            "search": True,
            "query": query,
        })
