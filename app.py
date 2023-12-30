from flask import Flask, flash, redirect, render_template, request, session, url_for
from functools import wraps
import csv, random
import os  # Don't forget to import os
from googletrans import Translator

# Configure application
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/AboutUs")
def AboutUs():
    return render_template("AboutUs.html")

@app.route("/AboutThem")
def AboutThem():
    return render_template("AboutThem.html")

@app.route("/AboutThem/FoodandNutrition")
def FoodandNutrition():
    return render_template("AboutThem/FoodandNutrition.html")

@app.route("/AboutThem/HealthandCare")
def HealthandCare():
    return render_template("AboutThem/HealthandCare.html")

@app.route("/AboutThem/Breeds")
def Breeds():
    return render_template("AboutThem/Breeds.html")

@app.route("/AboutThem/ItemsandToys")
def ItemsandToys():
    return render_template("AboutThem/ItemsandToys.html")

@app.route("/Organizations")
def Organizations():
    return render_template("Organizations.html")

@app.route("/DailyBunnyQuote")
def DailyBunnyQuote():
    with open('static/text/DailyBunnyQuote.csv', 'r') as file:
        reader = csv.reader(file, delimiter='|')
        next(reader)
        quotes = [{'quote': row[0].strip().replace('"', ''), 'author': row[1].strip().replace('"', '')} for row in reader]
        random_quote = random.choice(quotes)

    return render_template("DailyBunnyQuote.html", quote=random_quote['quote'], author=random_quote['author'])

@app.route('/<path:path>')
def catch_all(path):
    return render_template("Error404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
