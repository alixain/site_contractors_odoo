# Odoo 16 Contractors & Sites Module

## Description

This module allows you to manage **Contractors and their Sites** under a Company (res.partner) and link them to Sale Orders.

* Each **Company** can have multiple **Contractors**.
* Each **Contractor** can have multiple **Sites**.
* On **Sale Orders**, you can select the Contractor and the Site related to the Customer.
* Dynamic domains ensure only relevant Contractors and Sites are available for selection.
* Fully compatible with Odoo 16 Community Edition.

---

## Features

1. **Contractors Management**

   * Linked to a Company (Customer).
   * Add multiple Contractors under the Company.

2. **Sites Management**

   * Each Contractor can have multiple Sites.
   * Add Sites directly from the Contractor form view.

3. **Sale Order Integration**

   * Contractor field filtered by selected Customer.
   * Site field filtered by selected Contractor.
   * Adds Contractor and Site fields to the Sale Order form.

4. **Menus and Navigation**

   * Contractors menu under **Sales** module.
   * Easy navigation to Contractor and Site records.

5. **Security**

   * Standard access rights included for Contractors and Sites.

---

## Installation

1. Place the module folder into your Odoo addons path, e.g.:

   ```
   /odoo/custom_addons/site_contractors/
   ```
2. Restart the Odoo server:

   ```
   sudo systemctl restart odoo
   ```
3. Update Apps List from Apps menu.
4. Install **Site Contractors Module**.

---

## Usage

### 1. Add Contractors

* Go to **Contacts** → Open a Company → **Contractors Tab** → Create Contractor.

### 2. Add Sites

* Open a Contractor → **Sites Tab** → Add multiple Sites.

### 3. Create Sale Order

* Go to **Sales** → **Orders** → **Create**.
* Select Customer → Contractor → Site (filtered automatically).

---

## Dependencies

* **Odoo 16 Community Edition**
* **Sales module** (`sale`)

---

## Fields Added

### On res.partner

* `contractor_ids` (One2many to Contractors)

### On partner.contractor

* `partner_id` (Many2one to Company)
* `site_ids` (One2many to Sites)

### On partner.contractor.site

* `contractor_id` (Many2one to Contractor)

### On sale.order

* `contractor_id` (Many2one to Contractor, filtered by Customer)
* `site_id` (Many2one to Site, filtered by Contractor)

---

## Notes

* No custom plugin or external dependency required.
* Fully tested on Odoo 16 Community Edition.
* Clean module: installs without errors.

---

by Aspire Analytica
