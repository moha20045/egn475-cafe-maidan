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

SAMPLE_CART = [
    {
        "name": "Café con leche",
        "options": "Oat milk",
        "quantity": 2,
        "price_cents": 350,
    },
    {
        "name": "Guava pastelito",
        "options": None,
        "quantity": 1,
        "price_cents": 295,
    },
]

SAMPLE_KITCHEN_ORDERS = [
    {
        "order_id": 1040,
        "items": "1 × Cortadito",
        "status": "Ready",
    },
    {
        "order_id": 1041,
        "items": "1 × Guava pastelito",
        "status": "Preparing",
    },
    {
        "order_id": 1042,
        "items": "2 × Café con leche, 1 × pastelito",
        "status": "Received",
    },
]

SAMPLE_HISTORY = [
    {
        "id": 1037,
        "completed": "Today, 9:02 AM",
        "items": "1 × Guava pastelito",
        "status": "Picked up",
    },
    {
        "id": 1038,
        "completed": "Today, 9:15 AM",
        "items": "1 × Café con leche",
        "status": "Picked up",
    },
    {
        "id": 1039,
        "completed": "Today, 9:27 AM",
        "items": "2 × Cortadito",
        "status": "Picked up",
    },
]


@app.route("/", endpoint="home")
def home():
    return render_template("index.html")


@app.route("/menu", endpoint="menu")
def menu():
    return render_template("menu.html", items=SAMPLE_ITEMS)


@app.route("/order/new")
def order_new():
    total_cents = sum(
        item["price_cents"] * item["quantity"] for item in SAMPLE_CART
    )
    return render_template(
        "order.html", cart=SAMPLE_CART, total_cents=total_cents
    )


@app.route("/order/confirmation")
def order_confirmation():
    total_cents = sum(
        item["price_cents"] * item["quantity"] for item in SAMPLE_CART
    )
    confirmation = {
        "order_number": 1042,
        "status": "Received",
        "pickup_name": "Marta Rodriguez",
    }
    return render_template(
        "confirmation.html",
        confirmation=confirmation,
        cart=SAMPLE_CART,
        total_cents=total_cents,
    )


@app.route("/kitchen")
def kitchen():
    orders = sorted(SAMPLE_KITCHEN_ORDERS, key=lambda order: order["order_id"])
    return render_template("kitchen.html", orders=orders)


@app.route("/orders")
def orders():
    return render_template("history.html", history=SAMPLE_HISTORY)


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
