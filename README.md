# Café Calle Ocho — Ordering App Prototype

## Project description

Café Calle Ocho is a pickup-ordering prototype for a café in Little Havana. The project explores how online menu browsing and a kitchen order board could reduce counter lines, ordering mistakes, and confusion between customers and staff.

The customer persona is Marta Rodriguez, a regular café customer who wants coffee and breakfast ready for pickup. The staff persona is Carlos Perez, a kitchen employee who needs clear order details and status tracking.

## Project goals

The broader project scope includes viewing menu items and prices, choosing products and quantities, placing pickup orders, receiving an order confirmation and number, managing kitchen order statuses, viewing order history, and managing menu items.

Out of scope are online payments, delivery, SMS notifications, loyalty rewards, and a native mobile application.

## Setup

From the project directory, create and activate a virtual environment in PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run locally

```powershell
flask --app app run --debug
```

Open the local address printed by Flask, typically `http://127.0.0.1:5000/`.

## Routes

| Route | Page |
| --- | --- |
| `/` | Home |
| `/menu` | Café menu |
| `/menu/<int:item_id>` | Menu item details; unknown IDs return a custom 404 |
| `/order/new` | Sample order summary |
| `/order/confirmation` | Sample Order Confirmation |
| `/kitchen` | Kitchen Board |
| `/orders` | Completed Order History |
| `/about` | About text |

## Preview limitations

The menu, cart, kitchen orders, and history use sample data in `app.py`. Forms and status actions are previews only; the app does not save orders, change statuses, or use a database. The Order Confirmation route displays illustrative sample data and does not indicate that an order was submitted. Menu administration and other functional ordering behavior are not implemented.
