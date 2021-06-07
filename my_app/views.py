import requests
from requests.compat import quote_plus
from django.shortcuts import render
from . import models
from bs4 import BeautifulSoup

# Create your views here.

BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/search/?query={}'
def home(request):
    return render(request, 'base.html')


def new_search(request):
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    finl_url = BASE_CRAIGSLIST_URL.format(quote_plus(search))
    print(finl_url)
    response = requests.get(finl_url)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')
    post_titles = soup.find_all('a', {'class': 'result-title'})
    print(post_titles)
    stuff_for_frontend = {
        'search': search
    }
    return render(request, 'my_app/new_search.html', stuff_for_frontend)

def blog(request):
    return render(request, 'blog.html')