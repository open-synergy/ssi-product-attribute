# Create Product

> **Module:** ssi_product
>
> **Extends:** `product` (Odoo core) — model `product.template`
>
> **Model:** `product.template`
>
> **Menu:** Product & Pricelist > Products
>
> **Actor:** user in group _Product_

This work instruction documents only what `ssi_product` adds to `product.template`: the
**Brand** and **Sequence** fields on the product form, the **Brand** column in the
product list, and the **Brand** grouping in the search panel. Everything else on this
form is core Odoo behaviour and is not repeated here.

## Pre-Condition

- **Access:** User is in group _Product_.
- **Data:** The brand to select already exists as a `product.brand` record. Create it
  first through **Configuration > Product Categories & Attributes > Product Brands**
  (see `docs/product_brand/01-create.md`).
- **Module:** `ssi_product` is installed — without it the product form has no **Brand**
  field.

## Flow

1. Open the **Product & Pricelist > Products** menu. The product list is displayed with
   the **Brand** column added by this module.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields on the **General Information** tab:
   - **Product Name** _(required)_: Enter the name of the product.
   - **Brand**: Added by this module. Select the `product.brand` this product belongs
     to. Leaving it empty is allowed; when it is set, the brand is appended to the
     product's display name wherever the product is selected.
   - **Sequence**: Added to this form by this module. Enter the ordering number used
     when the product is displayed in a list.
4. Click **Save**.

## Post-Condition

- A new product record is created and its **Brand** is shown on the saved form.
- The product is listed with its brand in the **Brand** column of the product list.
- The product can be grouped by brand through the **Brand** entry of the search panel's
  **Group By** menu.

## Related Views

- On the product kanban card, the **Brand** value is rendered as a link that opens the
  `product.brand` record of that product. It only navigates — it changes nothing on the
  product itself.
