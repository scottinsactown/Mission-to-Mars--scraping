from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import pandas as pd

# Use Pymongo for CRUD applications for your database. For this homework, you can simply overwrite the existing document each time the `/scrape` url is visited and new data is obtained.

# make driver local and in github

# db = mongo.mars_db
# collection = db.mars_data

def init_browser():        
    executable_path = {"executable_path": "C:\Program Files\ChromeDriver\chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
# Establish connection
    browser = init_browser()
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    time.sleep(1)

# Mars news
    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Collect the latest news title and paragraph text
    news_title = soup.find('div', class_='content_title').text
    teaser = soup.find('div', class_='article_teaser_body').text

# Mars image
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    time.sleep(1)

    # Locate jpg through Full Image button
    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(2)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, 'html.parser')    
  
    # Collect the image url
    image = soup.find('div', class_='fancybox-inner')
    img_url = image.find('img')['src']
    img_start = 'https://www.jpl.nasa.gov'
    featured_image_url = img_start + img_url

# Mars weather
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, 'html.parser')

    # Collect latest weather
    tweet = soup.find('div', class_='js-tweet-text-container').text
    tweet_split = tweet.split('pic')
    mars_weather = tweet_split[0]

# Mars facts
    tables = pd.read_html('https://space-facts.com/mars/',match='Polar')
    mars_facts = tables[0]
    mars_facts.columns = ['description', 'value']
    mars_facts.set_index('description', inplace=True)
    mars_facts = mars_facts.to_html()
    mars_facts = mars_facts.replace("\n","")
    
# Mars hemispheres
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    time.sleep(1)
    hemis = ['Cerberus Hemisphere','Schiaparelli Hemisphere','Syrtis Major Hemisphere','Valles Marineris Hemisphere']
    hemisphere_image_urls = []
    for hemi in hemis:
        browser.click_link_by_partial_text(hemi)
        time.sleep(2)
        html = browser.html
        soup = bs(html, 'html.parser')
        title = hemi
        image_item = soup.find('li')
        image = image_item.a['href']
        hemisphere_image_urls.append({'title':title,'img_url':image})    
        browser.back()

# Store data in a dictionary
#     db.collection.upsert(
        mars_data = {
        "news_title": news_title,
        "news_p": teaser,
        "featured_image_url": featured_image_url,
        "mars_weather": mars_weather,
        "mars_facts": mars_facts,
        "hemisphere_image_urls": hemisphere_image_urls
    }
#     )

    browser.quit()

# Return results
    return mars_data
    print("done")
