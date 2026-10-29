# Import Flask so this file can use it.
from flask import Flask

# Create the Flask app for this file.
app = Flask(__name__)

# Connect the home URL to the home page.
@app.route("/")
# Define the function for the home page.
def home():
    # Send the welcome message to the browser.
    return "Welcome to Maidan Cafe"

# Connect the about URL to the about page.
@app.route("/about")
# Define the function for the about page.
def about():
    # Send the business description to the browser.
    return "Maidan Cafe is a welcoming café in South Florida."
