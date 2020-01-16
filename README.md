![Mission to Mars Header](https://github.com/scottinsactown/Mission-to-Mars--scraping/blob/master/Mission_top_med.jpg)

Web application that scrapes various websites for data related to the planet Mars and displays the information in a single HTML page using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.
* Jupyter Notebook file called `mission_to_mars.ipynb` demonstrates the scraping and analysis tasks.
  * NASA Mars News webpage scraped to collect the latest Mars-related News.
  * Featured Space Image webpage scraped to collect the current Featured Mars Image
  * Mars Weather twitter account scraped for the latest Mars weather tweet.
  * Mars Facts webpage scraped for a table containing facts about the planet including Diameter, Mass, etc.
  * USGS Astrogeology site scraped to obtain high resolution images for each of Mar's hemispheres.
  
* MongoDB with Flask templating used to create a new HTML page that displays all of the information that was scraped.
  * Jupyter notebook converted into a Python script called `scrape_mars.py` with a function called `scrape` that executes all scraping code and returns one Python dictionary containing all of the scraped data.
  * A route called `/scrape` imports the `scrape_mars.py` script and calls the `scrape` function.
  * Stores the return value in Mongo as a Python dictionary.
  * Created a root route that will query the Mongo database and pass the mars data into an HTML template to display the data.
  
* Created a template HTML index file that takes the Mars data dictionary and display all of the data in HTML elements.

![Mission to Mars Contet1](https://github.com/scottinsactown/Mission-to-Mars--scraping/blob/master/Mission_middle.jpg)
![Mission to Mars Content2](https://github.com/scottinsactown/Mission-to-Mars--scraping/blob/master/Mission_bottom.jpg)
