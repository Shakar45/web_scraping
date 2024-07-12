from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime
import os
import sys


application_path=os.path.dirname(sys.executable)
now=datetime.now()
month_date_year=now.strftime("%m%d%Y")


website="https://www.cricbuzz.com/"
path=r"C:\Users\Public\Desktop\Google Chrome.lnk"


# headless mode
options= Options()

options.headless=True

service=Service(execuitable_path=path)
driver=webdriver.Chrome(service=service, options=options)
driver.get(website)

containers=driver.find_elements(by="xpath",value='//div[@class="big-crd-main cb-bg-white cb-pos-rel"]')

titles=[]
subtitles=[]
links=[]


for container in containers:
    title=container.find_element(by="xpath",value='./h2').text
    subtitle=container.find_element(by="xpath",value='./h2').text
    link=container.find_element(by="xpath",value='./a').get_attribute('href')
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

my_dict={'title':titles,'subtitle':subtitles,'link':links}
df_headline=pd.DataFrame(my_dict)

filename=f"headline-{month_date_year}.csv"

final_path=os.path.join(application_path,filename)
df_headline.to_csv(final_path)

driver.quit()