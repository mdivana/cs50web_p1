from audioop import reverse
from curses import update_lines_cols
from multiprocessing.sharedctypes import Value
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from markdown2 import Markdown

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entrypage(request, entry):
    page = util.get_entry(entry)
    if page is None:
        return render(request, "encyclopedia/noenrty.html", {"entrytitle": entry})
    else:
        return render(request, "encyclopedia/entrypage.html", {
            "entry": Markdown().convert(page),
            "entrytitle": entry,
        })

def search(request):
    searchres = request.GET.get('q')
    if(util.get_entry(searchres) is not None):
        return HttpResponseRedirect(reverse('entry', kwargs = {'entry': searchres }))
    else:
        entrylist = []
        for entry in util.list_entries():
            if searchres.lower() in entry.lower():
                entrylist.append(entry)

        return render(request, "encyclopedia?index.html", {
            "entries": entrylist,
            "search": True,
            "value": searchres
        })
