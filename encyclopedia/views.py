from curses import update_lines_cols
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
