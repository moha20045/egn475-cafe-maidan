# EGN 475 - Week 2 Assignment 2.2
## My AI activity log - Café Calle Ocho

The initial six static HTML pages were prepared with ChatGPT assistance. I then used GitHub Copilot in VS Code to review and correct each individual page. The entries below record my actual review prompts and Copilot's reported outcomes; I am not claiming Copilot created the initial HTML files.

### Menu - commit `809e27d`

**My Copilot prompt:** Review my mockup/menu.html file for EGN 475 Café Calle Ocho. Remove the Order Confirmation link from the navigation, but keep the other five navigation links. Add a visible note explaining that quantities must be at least 1. Keep the existing menu items, milk dropdown, quantity input, Pico CSS, and links. Do not add JavaScript or backend code. Explain what you changed.

**Copilot reported:** Removed the Confirmation navigation link and added the quantity-minimum note.

**My verification:** I opened the page in a desktop browser, checked the visible layout and navigation, and committed the page separately as `809e27d`.

### Your Order - commit `fd67fef`

**My Copilot prompt:** Review mockup/order.html for my EGN 475 Café Calle Ocho project. Remove the Order Confirmation link from the navigation while keeping the other five links. Add a visible validation note explaining that the customer name cannot be blank when placing an order. Preserve the existing cart table, customer inputs, Pico CSS and navigation. Make sure the Place Order button links to confirmation.html and Back to Menu links to menu.html. Do not add JavaScript or backend code. Explain what you changed.

**Copilot reported:** Removed the Confirmation navigation link, added the customer-name note, preserved the cart, and checked the Place Order and Back to Menu links.

**My verification:** I opened the page in a desktop browser, checked the visible layout and navigation, and committed the page separately as `fd67fef`.

### Order Confirmation - commit `a2809d1`

**My Copilot prompt:** Review mockup/confirmation.html. Make only these changes: remove the Confirmation link from the navigation, keep the other five navigation links, and ensure the Order Again button links to menu.html. Do not rewrite the whole file. Do not change the existing order details, layout, Pico CSS, or other elements. Do not add JavaScript.

**Copilot reported:** Removed Confirmation from the header navigation and changed the existing button to Order Again, linked to menu.html.

**My verification:** I opened the page in a desktop browser, checked the visible layout and navigation, and committed the page separately as `a2809d1`.

### Kitchen Board - commit `01109ac`

**My Copilot prompt:** Review mockup/kitchen.html for my EGN 475 Café Calle Ocho assignment. Make only these changes: remove Confirmation from the navigation while keeping five links, add a visible empty-state example note saying No active orders, and match the sample kitchen rows to the wireframe. Preserve the three-row order table, status labels, Pico CSS and Order History link. Do not rewrite the whole file or add JavaScript or backend code. Explain your changes.

**Copilot reported:** Removed Confirmation from navigation; added No active orders; aligned the items for order #1042.

**My verification:** I opened the page in a desktop browser, checked the visible layout and navigation, and committed the page separately as `01109ac`.

### Order History - commit `78d6566`

**My Copilot prompt:** Review mockup/history.html for my EGN 475 Café Calle Ocho assignment. Remove Confirmation from the navigation, keeping the five main links. Preserve the existing two-row order history table and sample data. Ensure Back to Kitchen Board links to kitchen.html. Preserve Pico CSS and semantic HTML. Do not rewrite the entire file or add JavaScript or backend code. Explain exactly what changed and verify the links.

**Copilot reported:** Removed Confirmation from navigation, preserved both history rows, and kept the kitchen return link.

**My verification:** I opened the page in a desktop browser, checked the visible layout and navigation, and committed the page separately as `78d6566`.

### Menu Admin - commit `bfa8e7f`

**My Copilot prompt:** Review mockup/admin.html for my EGN 475 Café Calle Ocho assignment. Remove the Confirmation navigation link while retaining the other five links. Preserve both dropdowns, menu item name, description and price inputs, existing sample data, Pico CSS and semantic HTML. Ensure Preview Customer Menu links to menu.html. Do not rewrite the file or add JavaScript or backend code. Explain the changes and verify the required elements.

**Copilot reported:** Removed Confirmation from navigation and preserved the availability dropdowns, form fields, and customer-menu link.

**My verification:** I opened the page in a desktop browser, checked the visible layout and navigation, and committed the page separately as `bfa8e7f`.

**Prototype scope:** The HTML pages use realistic sample data. Form submission and kitchen status changes are nonfunctional until a backend is added.
