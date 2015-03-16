from dataomaha.models import * 
from django.shortcuts import * 
from django.db.models import * 
import tweepy
import time
from datetime import timedelta, date

def Main(request):
    auth = tweepy.OAuthHandler('h6LfPG4hTEI4mh1lY9BNodWdQ', 'W79YUWwPO3DM7IwLsbdCxvCN8fDLz2UYvwvNUG38skzsPqAnBL')
    auth.set_access_token('2873393133-RxBNfEOmtb6OXP4bRy5w3qkATiuwyBhu8e4dVFY', 'RjQOXWJUxm2w3SPEdDsav1wVXEcNeS4GrNqn4P9Ebd2Wn')
    sections = Section.objects.all().order_by('name')
    apps = App.objects.all().order_by('-section_feature')
    timestamp = time.strftime("%H:%M:%S")
    api = tweepy.API(auth)
    tweets = api.user_timeline('dataomaha')
    
    dictionaries = { 'sections': sections, 'apps': apps, 'timestamp': timestamp, 'tweets': tweets, }
    return render_to_response('dataomaha/main.html', dictionaries)


def Social(request):
    auth = tweepy.OAuthHandler('h6LfPG4hTEI4mh1lY9BNodWdQ', 'W79YUWwPO3DM7IwLsbdCxvCN8fDLz2UYvwvNUG38skzsPqAnBL')
    auth.set_access_token('2873393133-RxBNfEOmtb6OXP4bRy5w3qkATiuwyBhu8e4dVFY', 'RjQOXWJUxm2w3SPEdDsav1wVXEcNeS4GrNqn4P9Ebd2Wn')
    last24 = datetime.datetime.now()-timedelta(hours=30)
    last_week = datetime.datetime.now()-timedelta(days=7,hours=6)
    last_month = datetime.datetime.now()-timedelta(days=30,hours=6)
    api = tweepy.API(auth)
    list = []
    members = tweepy.Cursor(api.list_members, owner_screen_name='@owhnews', slug='owh-faces').items()
    for member in members:
        a = {}
        a['user'] = member
        list.append(a)
    count = len(list)
    timeline = api.list_timeline(owner_screen_name='@owhnews', slug='owh-faces')
    
    dictionaries = { 'members': members, 'list': list, 'count': count, 'timeline': timeline, 'last24': last24, 'last_week': last_week, 'last_month': last_month, }
    return render_to_response('dataomaha/twitter.html', dictionaries)
	
def Bio(request, username):
    username = username
    auth = tweepy.OAuthHandler('h6LfPG4hTEI4mh1lY9BNodWdQ', 'W79YUWwPO3DM7IwLsbdCxvCN8fDLz2UYvwvNUG38skzsPqAnBL')
    auth.set_access_token('2873393133-RxBNfEOmtb6OXP4bRy5w3qkATiuwyBhu8e4dVFY', 'RjQOXWJUxm2w3SPEdDsav1wVXEcNeS4GrNqn4P9Ebd2Wn')
    api = tweepy.API(auth)
    tweets = api.user_timeline(username)
    user = tweets[0].user
	
    dictionaries = { 'username': username, 'user': user, }
    return render_to_response('dataomaha/twitter-bio.html', dictionaries)
