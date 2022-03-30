#!/usr/bin/python3

import requests, json, sys, os, pyttsx3
from bs4 import BeautifulSoup


def get_last_page_link():

    url = 'https://www.twoism.org/forum/viewtopic.php?f=2&t=13222&sid=e4486184d2aa1e7a710e69a95e36d441'

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'lxml')

    results = soup.body

    page_number_links = results.find_all(class_='pagination')[0].find_all('a')[-1]['href']

    return page_number_links


if __name__ == '__main__':

    last_page_url = 'https://www.twoism.org/forum/viewtopic.php?f=2&t=13222&start=220'
    last_page = requests.get(last_page_url)
    last_page_soup = BeautifulSoup(last_page.content, 'lxml')
    last_page_posts = last_page_soup.body.find('div', id='wrap').find(id='page-body').find_all(class_='post')

    print(len(last_page_posts))


"""
    engine = pyttsx3.init()
    engine.say("post" + str(4))
    engine.runAndWait()
"""

"""
    new_url = 'https://www.twoism.org/forum/viewtopic.php?f=2&t=13222&start=220'
    new_page = requests.get(new_url)
    new_soup = BeautifulSoup(new_page.content, 'lxml')
    new_results = new_soup.body
    posts = new_results.find('div', id='wrap').find(id='page-body').find_all(class_='post')[-3].find(class_='postbody').find(class_='content').get_text()
    engine.say(posts)
    engine.runAndWait()
    #print(posts)
    """
