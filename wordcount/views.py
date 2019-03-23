from django.http import HttpResponse
from django.shortcuts import render
import operator
import re

def home(request):
    return render(request, "home.html")

def count(request):
    fulltext = request.GET["fulltext"]
    wordlist = fulltext.lower()
    worddictionary = {}
    for word in wordlist.split():
        if word.isalpha():
            if word in worddictionary:
                worddictionary[word] += 1
            else:
                worddictionary[word] = 1
    sorted_words = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, "count.html", {"fulltext":fulltext, "count":len(wordlist),"sortedwords":sorted_words})

def about(request):
    return render(request, "about.html")
