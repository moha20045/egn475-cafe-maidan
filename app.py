# Import Flask helpers for the app and its templates.
from flask import Flask, abort, render_template

# Create the Flask app for this file.
app = Flask(__name__)

SAMPLE_ITEMS = [
    {
        "id": 1,
        "name": "Café con leche",
        "description": "Espresso with warm milk.",
        "category": "coffee",
        "price_cents": 350,
        "available": True,
    },
    {
        "id": 2,
        "name": "Cortadito",
        "description": "Strong Cuban espresso softened with steamed milk.",
        "category": "coffee",
        "price_cents": 275,
        "available": True,
    },
    {
        "id": 3,
        "name": "Guava pastelito",
        "description": "Flaky pastry filled with guava.",
        "category": "bakery",
        "price_cents": 295,
        "available": True,
    },
    {
        "id": 4,
        "name": "Ham croqueta",
        "description": "Crispy Cuban-style ham croquette.",
        "category": "snacks",
        "price_cents": 195,
        "available": False,
    },
    {
        "id": 5,
        "name": "Café Cubano",
        "description": "Rich Cuban espresso with a sweet crema.",
        "category": "coffee",
        "price_cents": 225,
        "available": True,
    },
    {
        "id": 6,
        "name": "Mariquitas",
        "description": "Crispy plantain chips served as a café snack.",
        "category": "snacks",
        "price_cents": 250,
        "available": True,
    },
]


@app.route("/", endpoint="home")
def home():
    return render_template("index.html")


@app.route("/menu", endpoint="menu")
def menu():
    return render_template("menu.html", items=SAMPLE_ITEMS)


@app.route("/menu/<int:item_id>")
def item_detail(item_id):
    item = next((sample for sample in SAMPLE_ITEMS if sample["id"] == item_id), None)
    if item is None:
        abort(404)
    return render_template("item.html", item=item)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.route("/about")
def about():
    return "Maidan Cafe is a welcoming café in South Florida."
