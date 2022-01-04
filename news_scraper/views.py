from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import News

def news_list(request):
    try:
        page = requests.get("https://www.irna.ir/archive?pl=2300")
        soup = BeautifulSoup(page.content, 'html.parser')
        
        news_titles=soup.select("#box4 h3 a")
        titles = [nt.get_text() for nt in news_titles]

        img_list = soup.select("#box4 img")
        imgs = [il.get('src') for il in img_list]

        news_leads=soup.select(".desc p")
        leads = [nl.get_text() for nl in news_leads]
        
        for i in range(30):
            str=leads[i]
            x= str.rfind('-')
            leads[i]= str[x+1:]

        news_times=soup.select("time a")
        times = [nt.get_text() for nt in news_times]

        news = [['' for i in range(4)] for j in range(30)]
        for i in range(30):
            news[i][0]=titles[i]
            news[i][1]=imgs[i]
            news[i][2]=leads[i]
            news[i][3]=times[i]
            
        return render(request, 'news_scraper/news_list.html', {'news':news})

    except:
        db_news = News.objects.order_by('time')
        return render(request, 'news_scraper/news_list_db.html', {'db_news':db_news})
