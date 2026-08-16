# Create Product Variant

> **Module:** ssi_product
>
> **Extends:** `product` (Odoo core) — model `product.product`
>
> **Model:** `product.product`
>
> **Menu:** Product & Pricelist > Product Varians
>
> **Actor:** user in group _Product_

This work instruction documents only what `ssi_product` adds to `product.product`: the
drag handle and the **Brand** column in the variant list, and the **Brand** and
**Sequence** fields on the variant form. Everything else on this form is core Odoo
behaviour and is not repeated here.

## Pre-Condition

- **Access:** User is in group _Product_.
- **Data:** The brand to select already exists as a `product.brand` record. Create it
  first through **Configuration > Product Categories & Attributes > Product Brands**
  (see `docs/product_brand/01-create.md`).
- **Module:** `ssi_product` is installed — without it the variant list has no **Brand**
  column and the variant form has no **Brand** field.

## Flow

1. Open the **Product & Pricelist > Product Varians** menu. The variant list is
   displayed with the drag handle and the **Brand** column added by this module.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields on the **General Information** tab:
   - **Product Name** _(required)_: Enter the name of the variant.
   - **Brand**: Added by this module. Select the `product.brand` this variant belongs
     to. Leaving it empty is allowed; when it is set, the brand is appended to the
     variant's display name wherever the variant is selected.
   - **Sequence**: Added to this form by this module. Enter the ordering number used
     when the variant is displayed in a list.
4. Click **Save**.

## Post-Condition

- A new product variant record is created and its **Brand** is shown on the saved form.
- The variant is listed with its brand in the **Brand** column of the variant list.
- Variants are ordered by category first, then by **Sequence** — the model is ordered by
  `categ_id, sequence, default_code, name, id` once this module is installed, and the
  order can afterwards be changed by dragging the handle in the variant list.

## Related Views

- On the variant kanban card, the **Brand** value is rendered as a link that opens the
  `product.brand` record of that variant. It only navigates — it changes nothing on the
  variant itself.
