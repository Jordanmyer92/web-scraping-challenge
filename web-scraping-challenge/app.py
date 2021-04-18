from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")
@app.route("/")
def index():
    marsdata = mongo.db.mars_db.find_one()
    return render_template("index.html", marsdata_html = marsdata)


@app.route("/scrape")
def scrape():
    marsdata_sp = scrape_mars.scrape()
    mongo.db.mars_db.update({}, marsdata_sp, upsert=True)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)