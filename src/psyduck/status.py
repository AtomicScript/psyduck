# GET THE STATUS NEEDED
import requests
import json
from bs4 import BeautifulSoup

# returns a dictionay
def get_vocab_status():
    response = requests.get('https://api.vocabulary.com/1.0/leaderboards/individual/points/weekly/20221203?uid=A00SZ9M15P1FVM&top=0', headers={ 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2NzAwMjE5MTYsImV4cCI6MTY3MDA0MzUxNiwianRpIjoieGEyNzUxZGZjMzA3YWE4MGU2MjNiYTMyODEwMWEyMjA1In0.pvHVq2uD2WBEKB1SXIEvcmxVTqjc8D7cat-IVsZV218' })
    # converts from str to dict
    info = json.loads(response.text)['me']
    return info

# returns level and rank in a dict
##! TO DO: ADD THIS TO GITHUB PAGE
# image badge :  <img src="https://tryhackme-badges.s3.amazonaws.com/Atom87.png" alt="TryHackMe">
def get_thm_status():
    doc = BeautifulSoup(requests.get('https://tryhackme.com/p/Atom87').text, 'html.parser')
    level = doc.find_all('div', {'class': 'size-30 bold'})[2].text
    rank = json.loads(requests.get('https://tryhackme.com/api/user/rank/Atom87').text)['userRank']
    info = {'level': level, 'rank': rank}
    return info

def get_htb_status():
    # if you get 404 you can update the header since this user-agent is custom!
    headers = {'User-Agent': 'Custom'}
    htb = 'https://www.hackthebox.com/api/v4/profile/600209'
    with requests.Session() as s:   
        info = json.loads(s.get(htb, headers=headers).text)
        return info

# https://hsk.academy/en/hsk-1-vocabulary-list
def set_chinese_learning(chinese_char, words, pinyin, grammar):
    info = {
    'Character': str(chinese_char), 
    'words': str(words),
    'pinyin': str(pinyin),
    'Grammar': str(grammar),
    }
    return info

def set_Japanese_Learning(lessons, assessments,words, grammar, kanji, books_read):
    info = {
    'Lessons': str(lessons), 
    'Assessments': str(assessments),
    'words': str(words),
    'Grammar': str(grammar),
    'kanji': str(kanji),
    'Books Read':str(books_read),
    }
    return info



def get_HBM():
    headers = {'User-Agent': 'Custom'}
    url = 'https://humanbenchmark.com/users/61b6f92a474fe8000986951c'
    # status = ['/reactiontime', '/memory', '/number-memory', '/verbal-memory', '/typing', '/aim','/chimp', '/sequence']

    with requests.Session() as session:
        doc = session.get(url)
        print(doc.json())


get_HBM()