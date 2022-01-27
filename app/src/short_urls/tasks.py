import time
import sqlite3
import requests
from bs4 import BeautifulSoup

def threaded_task(shorterObj):
  title = get_title_from_page(shorterObj.original_url)
  add_title_to_database(shorterObj.id, title)
    
def add_title_to_database(id, title):
  con = sqlite3.connect('app/src/core/flask_boilerplate_main.db')
  cur = con.cursor()
  cur.execute("UPDATE short_urls SET page_title = :title WHERE id = :id", {'id': id, 'title': title})
  con.commit()
  con.close()

def get_title_from_page(url):
  try:
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    title = soup.find('title').text
    return title
  except:
    print('error')