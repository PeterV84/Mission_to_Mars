#!/usr/bin/env python
# coding: utf-8




# Import Splinter and BeautifulSoup
from splinter import Browser

from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

from bs4 import BeautifulSoup as soup

import datetime as dt
from webdriver_manager.chrome import ChromeDriverManager


def scrape_all():
    # Initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    news_title, news_paragraph = mars_news(browser)

     #Run all scraping functions and store results in a dictionary
    data = {
        'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg',
    'title': 'Cerberus Hemisphere Enhanced',
    'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg',
    'title': 'Schiaparelli Hemisphere Enhanced',
    'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg',
    'title': 'Syrtis Major Hemisphere Enhanced',
    'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg',
  'title': 'Valles Marineris Hemisphere Enhanced'
  }

    

    # Stop webdriver and return data
    browser.quit()
    return data
#if __name__ == "__main__":
    # If running as script, print scraped data
   # print(scrape_all())


#executable_path = {'executable_path': ChromeDriverManager().install()}
#browser = Browser('chrome', **executable_path, headless=False)




# Visit the mars nasa news site
def mars_news(browser):
    
      # Visit the mars nasa news site
   url = 'https://redplanetscience.com/'
   browser.visit(url)

   # Optional delay for loading the page
   browser.is_element_present_by_css('div.list_text', wait_time=1)

   # Convert the browser html to a soup object and then quit the browser
   html = browser.html
   news_soup = soup(html, 'html.parser')

   slide_elem = news_soup.select_one('div.list_text')

   # Use the parent element to find the first <a> tag and save it as `news_title`
   news_title = slide_elem.find('div', class_='content_title').get_text()

   # Use the parent element to find the paragraph text
   news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

   return news_title, news_p
 # Add try/except for error handling
   try:
        slide_elem = news_soup.select_one('div.list_text')
        # Use the parent element to find the first 'a' tag and save it as 'news_title'
        news_title = slide_elem.find('div', class_='content_title').get_text()
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
        
   except AttributeError:
        return None, None



#html = browser.html
##news_soup = soup(html, 'html.parser')
#slide_elem = news_soup.select_one('div.list_text')




#slide_elem.find('div', class_='content_title')




# Use the parent element to find the first `a` tag and save it as `news_title`
#news_title = slide_elem.find('div', class_='content_title').get_text()
#news_title





# Use the parent element to find the paragraph text
#news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
#news_p





# Visit URL
def featured_image(browser):
    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError:
        return None

    # Use the base url to create an absolute url
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'

    return img_url




# Find and click the full image button
#@full_image_elem = browser.find_by_tag('button')[1]
#full_image_elem.click()





# Parse the resulting html with soup
#html = browser.html
#img_soup = soup(html, 'html.parser')





# Find the relative image url
#img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
##img_url_rel





# Use the base URL to create an absolute URL
def mars_facts():
    # Add try/except for error handling
    try:
        # Use 'read_html' to scrape the facts table into a dataframe
        df = pd.read_html('https://galaxyfacts-mars.com')[0]

    except BaseException:
        return None

    # Assign columns and set index of dataframe
    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)

    # Convert dataframe into HTML format, add bootstrap
    return df.to_html()

def hemisphere():
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    browser.visit(url)
# Convert dataframe into HTML format, add bootstrap
    return df.to_html()

# In[21]:



def hemisphere():
# 1. Use browser to visit the URL 
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    browser.visit(url)

# 3. Write code to retrieve the image urls and titles for each hemisphere.
#for loop 
    for i in range(4):
    #create empty dictionary
        hemispheres = {}
    # Optional delay for loading the page
    #browser.is_element_present_by_css('div.list_text', wait_time=1)
    #browser.css('a.ite MLink product-item h3')
    
        browser.find_by_css('a.product-item h3')[i].click()
    
        element = browser.find_link_by_text('Sample').first
    #img_url = f'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars{img_url_rel}'

    #return img_url

        img_url = element['href']
    #title = browser.find_by_css("h2.title").text
    
        hemispheres["img_url"] = img_url
        hemispheres["title"] = title
        hemisphere_image_urls.append(hemispheres)
    
        browser.back()

    data = {
        'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg',
        'title': 'Cerberus Hemisphere Enhanced',
        'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg',
        'title': 'Schiaparelli Hemisphere Enhanced',
        'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg',
        'title': 'Syrtis Major Hemisphere Enhanced',
        'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg',
    'title': 'Valles Marineris Hemisphere Enhanced'
    }

    return hemisphere
#def scrape_hemisphere(html_text):
    # parse html text
    #hemi_soup = soup(html_text, "html.parser")
    # adding try/except for error handling
    #try:
       # title_elem = hemi_soup.find("h2", class_="title").get_text()
       # sample_elem = hemi_soup.find("a", text="Sample").get("href")
   # except AttributeError:
        # Image error will return None, for better front-end handling
       # title_elem = None
       # sample_elem = None
   # hemispheres = {
       # "title": title_elem,
       # "img_url": sample_elem
    #}
   # return hemispheres


#df = pd.read_html('https://galaxyfacts-mars.com')[0]
#df.columns=['description', 'Mars', 'Earth']
#df.set_index('description', inplace=True)
#df




#df.to_html()



if __name__ == "__main__":

    # If running as script, print scraped data
    print(scrape_all())
    Browser.quit()


# In[ ]:




