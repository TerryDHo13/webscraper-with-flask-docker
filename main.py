from flask import Flask, render_template
from scraper import scraper

app = Flask(__name__, template_folder='pages')

#displays the home.html
@app.route("/")
def run():
    return render_template("home.html")

#display the scrape.html with the result after scrapping
@app.route("/scrape")
def scrape():
    number = scraper()
    return render_template("scrape.html", number=number)

if __name__== "__main__":
    app.run(debug=True)