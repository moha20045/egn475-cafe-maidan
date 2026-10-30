# Café Calle Ocho — User Stories and Acceptance Criteria

**EGN 475 | Week 2 | Assignment 2.1**
**Project:** Option A — Café Calle Ocho (Little Havana)
**Repository:** https://github.com/moha20045/egn475-cafe-maidan

## Project context
This backlog turns the Week 1 Café Calle Ocho scope into small, testable user stories for a pickup-ordering prototype. Marta Rodriguez is the regular-customer persona, and Carlos Perez is the kitchen-employee persona. Manager stories cover the separate administrative capability from the Week 1 feature list. Must stories establish the minimum usable ordering flow; should and could stories can follow after the core flow works.

## Story priorities
- **Must:** required for the first working pickup-ordering prototype.
- **Should:** important enhancements once the core order flow works.
- **Could:** additional menu-management convenience if time allows.

## Backlog

### ST-01 — Must
**Story:** As a Customer (Marta), I want to browse the café menu with prices and descriptions, so that I can choose what to order.

**Acceptance criterion 1 — expected behavior**
- Given the café has menu items available, When I open the menu, Then I see each available item’s name, description, and price.

**Acceptance criterion 2 — error or edge case**
- Given no items are currently available, When I open the menu, Then I see a clear “No items available” message instead of a blank or broken page.

### ST-02 — Must
**Story:** As a Customer (Marta), I want to choose the quantity and available milk type for one drink, so that my pickup order matches my preferences.

**Acceptance criterion 1 — expected behavior**
- Given café con leche is available with whole milk and oat milk options, When I choose oat milk and quantity two, Then the order selection shows two café con leche drinks with oat milk.

**Acceptance criterion 2 — error or edge case**
- Given I select an available café con leche, When I try to add a quantity of zero or less, Then the item is not added and I see “Quantity must be at least 1.”

### ST-03 — Must
**Story:** As a Customer (Marta), I want to review my selected items before I order, so that I can catch mistakes before sending the order.

**Acceptance criterion 1 — expected behavior**
- Given I have selected two items, When I open the order summary, Then I see each item, its quantity, options, and price.

**Acceptance criterion 2 — error or edge case**
- Given my selection is empty, When I open the order summary, Then I see an empty-order message and cannot submit it.

### ST-04 — Must
**Story:** As a Customer (Marta), I want to place an order for café pickup, so that I can avoid waiting in the counter line.

**Acceptance criterion 1 — expected behavior**
- Given my order contains at least one available item, When I confirm a pickup order, Then it is accepted with a starting status of Received.

**Acceptance criterion 2 — error or edge case**
- Given an item becomes sold out before I confirm, When I submit the order, Then it is not accepted and I am told which item is unavailable.

### ST-05 — Must
**Story:** As a Customer (Marta), I want to receive a confirmation with an order number, so that I know the café received my pickup request.

**Acceptance criterion 1 — expected behavior**
- Given my pickup order was accepted, When the confirmation appears, Then it displays the order number and an accurate item summary.

**Acceptance criterion 2 — error or edge case**
- Given an order was not accepted, When I try to view its confirmation, Then no confirmation number is shown and I see an error message.

### ST-06 — Should
**Story:** As a Customer (Marta), I want to check the current status of my pickup order, so that I know when to collect it.

**Acceptance criterion 1 — expected behavior**
- Given my order is marked Ready, When I check its status using the order number, Then I see Ready.

**Acceptance criterion 2 — error or edge case**
- Given I enter an order number that does not exist, When I check its status, Then I see “Order not found” without another order’s details.

### ST-07 — Must
**Story:** As a Kitchen staff (Carlos), I want to see all active pickup orders ordered by their order number, so that I can prepare the oldest orders first.

**Acceptance criterion 1 — expected behavior**
- Given three active orders include two submitted at the same time, When I open the kitchen board, Then I see all active orders (Received, Preparing, and Ready) in ascending order-number sequence, including the lower-numbered simultaneous order first.

**Acceptance criterion 2 — error or edge case**
- Given there are no active orders, When I open the kitchen board, Then I see a “No active orders” message.

### ST-08 — Must
**Story:** As a Kitchen staff (Carlos), I want to advance an order to its next allowed status, so that the team can track each order’s progress accurately.

**Acceptance criterion 1 — expected behavior**
- Given an order is Received, Preparing, or Ready, When I select the available next-step action, Then its status changes respectively to Preparing, Ready, or Picked up on the kitchen board.

**Acceptance criterion 2 — error or edge case**
- Given an order is already Picked up, When I attempt another status change, Then the status remains Picked up and the system prevents the change with a clear message.

### ST-09 — Should
**Story:** As a Kitchen staff (Carlos), I want to review orders that were picked up, so that I can check past work without cluttering the active board.

**Acceptance criterion 1 — expected behavior**
- Given an order was marked Picked up, When I open order history, Then that order appears with its number and final status.

**Acceptance criterion 2 — error or edge case**
- Given no orders have been picked up, When I open order history, Then I see “No completed orders yet.”

### ST-10 — Should
**Story:** As a Café manager, I want to mark a menu item as sold out or available, so that customers cannot order products the café cannot prepare.

**Acceptance criterion 1 — expected behavior**
- Given a menu item is available, When I mark it Sold out, Then customers see it as unavailable and cannot select it.

**Acceptance criterion 2 — error or edge case**
- Given a customer or kitchen staff account is signed in (rather than a manager account), When that person tries to mark an item sold out or available, Then the item remains unchanged and an “Access denied” message appears.

### ST-11 — Could
**Story:** As a Café manager, I want to add a new menu item, so that customers can discover new offerings.

**Acceptance criterion 1 — expected behavior**
- Given I enter a name, description, and valid nonnegative price, When I save the new item, Then it appears in the café menu.

**Acceptance criterion 2 — error or edge case**
- Given the item name is blank, When I try to save a new item, Then the item is not created and the name field is identified as required.

### ST-12 — Could
**Story:** As a Café manager, I want to update the price of an existing menu item, so that customers see the correct price.

**Acceptance criterion 1 — expected behavior**
- Given I am signed in as a manager and a menu item costs $4.00, When I change its price to $4.50 and save, Then the menu displays $4.50 for that item.

**Acceptance criterion 2 — error or edge case**
- Given an existing menu item costs $4.50, When I enter a negative price and try to save, Then the change is rejected, the displayed price stays $4.50, and I see “Price must be zero or greater.”

## Suggested build order
ST-01 → ST-02 → ST-03 → ST-04 → ST-05 → ST-07 → ST-08 → ST-06 → ST-09 → ST-10 → ST-11 → ST-12

## Backlog review notes
The broader Week 1 menu-management feature was split into ST-10 (availability), ST-11 (adding items), and ST-12 (price editing). After Copilot reviewed the draft on October 30, 2026, the five flagged stories (ST-02, ST-07, ST-08, ST-10, and ST-12) were revised to define options, ordering, status changes, role permissions, and price validation. The corresponding screenshot and suggested accept decisions are documented in the accompanying report. These changes should be reviewed by the student before committing.
