# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def scrape(): 
# %%
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


# %%
    url = "https://redplanetscience.com/"
    browser.visit(url)


# %%
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")


# %%
    #print(soup.body.prettify())


# %%
    news_title = soup.find_all("div", class_="list_text")[0].find("div", class_="content_title").text

    #news_title


# %%
    news_p = soup.find_all("div", class_="list_text")[0].find("div", class_="article_teaser_body").text

    #news_p


# %%
    url = "https://spaceimages-mars.com/"
    browser.visit(url)


# %%
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")


# %%
    print(soup.body.prettify())


# %%
#<div class="header">
#<div class="floating_text_area">
#<a class="showimg fancybox-thumbs" href="image/featured/mars2.jpg" target="_blank">
#featured_image_url = soup.find("div", class_="header").find("div", class_="floating_text_area").find("a", class_="showing fancybox-thumbs").href

    featured_image_url = soup.find("div", class_="header").find("div", class_="floating_text_area").a.get("href")
                               
    #featured_image_url                               


# %%
    url = "https://galaxyfacts-mars.com/"
    browser.visit(url)


# %%
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")


# %%
    tables = pd.read_html(url)
    #tables


# %%
    type(tables)


# %%
    df = tables[0]
    #df.head()


# %%
    html_table = df.to_html()
    #html_table


# %%
    url = "https://marshemispheres.com/"
    browser.visit(url)


# %%
    soup = BeautifulSoup(html, "html.parser")


# %%
    #print(soup.body.prettify())


# %%
    #image_url_list = []
    #links = soup.find_all("img")
    #links


# %%
#<div class="container-fluid site-content" style="margin-top: 150px;">
#<img class="img-fluid" src="https://space-facts.com/wp-content/uploads/mars.jpg"/>
#<img src="https://space-facts.com/wp-content/uploads/mars-size.png" width="90%"/>
#<img src="https://space-facts.com/wp-content/uploads/mars-orbit.png" width="90%"/>
#<img class="img-fluid" src="https://i1.wp.com/space-facts.com/wp-content/uploads/terrestrial-planet-orbits.png?resize=350%2C200&amp;ssl=1" style="padding: 0px;"/>    
    hemisphere_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": "https://marshemispheres.com/images/4e59980c1c57f89c680c0e1ccabbeff1_valles_marineris_enhanced.tif_thumb.png"},
        {"title": "Cerberus Hemisphere", "img_url": "https://marshemispheres.com/images/39d3266553462198bd2fbc4d18fbed17_cerberus_enhanced.tif_thumb.png"},
        {"title": "Schiaparelli Hemisphere", "img_url": "https://marshemispheres.com/images/08eac6e22c07fb1fe72223a79252de20_schiaparelli_enhanced.tif_thumb.png"},
        {"title": "Syrtis Major Hemisphere", "img_url": "https://marshemispheres.com/images/55a0a1e2796313fdeafb17c35925e8ac_syrtis_major_enhanced.tif_thumb.png"}
    ]

    hemisphere_image_urls


# %%
    marsdata_html = {
        "news_title":news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "df": df,
        "hemisphere_image_urls": hemisphere_image_urls
    
    
    }


# %%
# Quit the browser
    browser.quit()


# %%
    return marsdata_html 


