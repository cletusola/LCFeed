from django.shortcuts import render
from django.http import HttpResponse
from .models import TodayFeed
from django.contrib.auth.decorators import login_required 

from datetime import date
import requests
import json
import os  
from dotenv import load_dotenv


load_dotenv('../.env')

# function to fetch news feeds 
def getdata():

    url = "https://daily-mail-feed.p.rapidapi.com/api/news/daily-mail/%7Bcategory%7D"
    headers = {
        "X-RapidAPI-Key": os.getenv('API_KEY'),
        "X-RapidAPI-Host": "daily-mail-feed.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    data = json.loads(response.text)

    for i in range(72):
        title = data[i]['title']
        description = data[i]['description']
        url = data[i]['url']
        date = data[i]['date']

        feed = TodayFeed.objects.create(
            title=title,description=description,url=url,date=date
        )
        feed.save()
        feeds = TodayFeed.objects.all().order_by('-time_fetched')[:70]
        if feeds:
            try:
                older_feed = TodayFeed.objects.all().order_by('time_fetched')[:73]
                older_feed.delete()
            except:
                pass
        else:
            pass 

    return None

# home view 
def HomeView(request):
    feeds = None
    today = date.today()
    feed = TodayFeed.objects.all().order_by('-time_fetched')[:1]
    if feed.count() > 0:
        for f in feed:
            if str(f.date_fetched) == str(today):
                feeds = TodayFeed.objects.all().order_by('-time_fetched')[:70]   
            else:
                getdata()
                feeds = TodayFeed.objects.all().order_by('-time_fetched')[:70] 
    else:
        try:
            getdata()
            feeds = TodayFeed.objects.all().order_by('-time_fetched')[:70] 
        except:
            return HttpResponse("Unable to fetch feeds from source, API error please try again later.")
    return render(request,'home.html',{'feeds':feeds})


    