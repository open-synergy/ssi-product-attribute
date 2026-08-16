# Create Product Category

> **Module:** ssi_product
>
> **Extends:** `product` (Odoo core) — model `product.category`
>
> **Model:** `product.category`
>
> **Menu:** Product & Pricelist > Configuration > Product Categories & Attributes >
> Categories
>
> **Actor:** user in group _Product Category_

This work instruction documents only what `ssi_product` adds to `product.category`: the
manual **Sequence** field. Everything else on this form is core Odoo behaviour and is
not repeated here.

## Pre-Condition

- **Access:** User is in group _Product Category_.
- **Module:** `ssi_product` is installed — without it `product.category` has no
  **Sequence** field and the list has no drag handle.

## Flow

1. Open the **Product & Pricelist > Configuration > Product Categories & Attributes >
   Categories** menu. The categories are displayed as a list whose first column is the
   drag handle added by this module.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Category name** _(required)_: Enter the name of the category.
   - **Sequence** _(required)_: Added by this module. Enter the ordering number of this
     category among its siblings. It defaults to **4**; a lower number puts the category
     earlier in every list of categories.
4. Click **Save**.

## Post-Condition

- A new product category record is created.
- The category is ordered by its **Sequence** value within its parent category — the
  model is ordered by `parent_id, sequence, id` once this module is installed.
- The **Sequence** value can afterwards be changed by dragging the handle in the
  category list instead of opening the form.
