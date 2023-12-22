from flask import Flask, flash, redirect, render_template, request, session, url_for
from functools import wraps
import os  # Don't forget to import os

# Configure application
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
