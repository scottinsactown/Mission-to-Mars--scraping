from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# # setup mongo connection
# conn = "mongodb://localhost:27017"
# client = pymongo.MongoClient(conn)

# # connect to mongo db and collection
# db = client.store_inventory
# collection = db.produce

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    planet_data = mongo.db.collection.find_one()
    return render_template("index.html", mars = planet_data)

# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

#     mars = mongo.db.mars
    
    # Run the scrape function
    mars_data = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
