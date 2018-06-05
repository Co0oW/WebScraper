from __future__ import unicode_literals
from bs4 import BeautifulSoup as bs
import requests, pickle, os, youtube_dl
import time, random
from selenium import webdriver

def downloadYoutube(listOfLinks):
    ydl_opts = {
        'format': 'bestaudio/best',
        'proxy': 'socks5://niwdle:Silverbullet19!@jfk-s01.vpn.asia:1080',
        'outtmpl': os.getcwd()+'/xKito Music - YouTube - YouTube/%(title)s.%(ext)s',
        'download_archive': 'downloaded.txt',
        # 'username': 'Niwdle',
        # 'password': 'Silverbullet19!!',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(listOfLinks)

def main():

    youtubeurl = 'https://www.youtube.com/user/nyuualiaslucy/videos'

    # testpage = urllib.urlopen(youtubeurl).read()
    # print testpage

    #Started to use Selenium to dynamically scrape for data
    #downloaded Geckodriver and copied to /usr/local/bin/
    session = webdriver.Firefox()
    session.get(youtubeurl)

    numPages = 10
    #scroll for x pages loop
    for x in range(1, numPages):
        positionOfPage = int(x)*1000
        session.execute_script('window.scrollTo(1,' + str(positionOfPage) + ');')
        print positionOfPage
        print 'window.scrollTo(1,' + str(x) + ');'
        time.sleep(random.random()*3 + 2)

    soup = bs(session.page_source, 'html.parser')
    links = soup.find_all('a', attrs={'class':"yt-simple-endpoint style-scope ytd-grid-video-renderer"})
    print len(links)


    if os._exists(os.getcwd()+'/'+session.title+'.pkl'):
        openFile = open(os.getcwd()+'/'+session.title+'.pkl', 'rb')
        linkTable = pickle.load(openFile)
        fileExists = True
    else:
        linkTable = []
        fileExists = False

    for link in links:
        videoData = (link.get('title'), link.get('href'))
        if videoData not in linkTable and link.get('title') != None:
            linkTable.append(videoData)


    if fileExists:
        openFile.close()

    openFile = open(os.getcwd()+'/'+session.title+'.pkl', 'wb')
    pickle.dump(linkTable, openFile)
    openFile.close()

    if not os._exists(os.getcwd()+'/'+session.title+'/'):
        os.makedirs(os.getcwd()+'/'+session.title)


def testLinkTable(filename):
    openFile = open(os.getcwd() + '/' + filename, 'rb')
    table = pickle.load(openFile)
    openFile.close()
    print table
    print len(table)

if __name__ == '__main__':
    # downloadYoutube()
    # main()
    # testLinkTable('xKito Music - YouTube - YouTube.pkl')
    pass