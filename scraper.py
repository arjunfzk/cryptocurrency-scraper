from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time
from bs4 import BeautifulSoup
binary = FirefoxBinary()
wd = webdriver.Firefox(firefox_binary=binary)

wdx = webdriver.Firefox(firefox_binary=binary)


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
x=4
# Start the WebDriver and load the page
while True:
    time.sleep(50)
    wd.get('https://koinex.in/')
    wdx.get('https://bitfinex.com/')


# Wait for the dynamically loaded elements to show up
    time.sleep(30)
#WebDriverWait(30)

# And grab the page HTML source
    html_page = wd.page_source
    html_pagex = wdx.page_source

   # wd.quit()
#print(html_page)
    soup=BeautifulSoup(html_page,'html.parser')
    x=soup.find_all('b',class_='ng-binding')

#print(x[0].get_text())
#print(x[1].get_text())
    z=x[0].get_text()[9:]
    z2=x[1].get_text()[9:]
    z=z.replace(',','')
    z2=z2.replace(',','')
    z=float(z)

    z2=float(z2)
    print((z))
    print((z2))

    soupx=BeautifulSoup(html_pagex,'html.parser')
    name_box = soupx.find('span', attrs={'title': 'BTC:USD Last Trade'})
    name_box2 = soupx.find('span', attrs={'title': 'ETH:USD Last Trade'})

    name=name_box.text.strip()
    name2=name_box2.text.strip()
    name=name.replace(',','')
    name2=name2.replace(',','')
    name=float(name)
    print(name)
    name2=float(name2)
    print(name2)
    btc="bitcoin ratio= "+str((z/name))
    eth="ether ratio = "+str((z2/name2))
    print(btc)
    print(eth)
  #  wdx.quit()
    import requests
    import json
 
    def send_notification_via_pushbullet(title, body):
        """ Sending notification via pushbullet.
            Args:
                title (str) : title of text.
                body (str) : Body of text.
        """
        data_send = {"type": "note", "title": title, "body": body}
 
        ACCESS_TOKEN = ''
        resp = requests.post('https://api.pushbullet.com/v2/pushes', data=json.dumps(data_send),
                             headers={'Authorization': 'Bearer ' + ACCESS_TOKEN, 'Content-Type': 'application/json'})
        if resp.status_code != 200:
            raise Exception('Something wrong')
        else:
            print ('complete sending')
    send_notification_via_pushbullet(btc+",\n"+eth,"bitcoin="+str(z)+"  ether="+str(z2)+"\n btc$ = "+str(name)+" "+"ether$ = "+str(name2))
