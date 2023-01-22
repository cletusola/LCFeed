from django.shortcuts import render
from django.http import HttpResponse
from .models import TodayFeed
from django.contrib.auth.decorators import login_required 


import requests
import json
import time


#news refresh view(can only be accessed by an auth user
@login_required
def getData(request):

    url = "https://daily-mail-feed.p.rapidapi.com/api/news/daily-mail/%7Bcategory%7D"

    headers = {
        "X-RapidAPI-Key": "8211bedd48mshaeec0f8548aac97p1c9a0djsn0a939a85759c",
        "X-RapidAPI-Host": "daily-mail-feed.p.rapidapi.com"
    }

    try:
        response = requests.request("GET", url, headers=headers)

        data = json.loads(response.text)

        for i in range(74):
            title = data[i]['title']
            description = data[i]['description']
            url = data[i]['url']
            date = data[i]['date']

            feed = TodayFeed.objects.create(
                title=title,description=description,url=url,date=date
            )
            feed.save()
    except:
        data = "Unable to fetch headlines"

    return HttpResponse("fetched")


def HomeView(request):
    feeds = TodayFeed.objects.all().order_by('-time_fetched')[:74]
    return render(request,'home.html',{'feeds':feeds})
