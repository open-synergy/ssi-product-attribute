# View Price Rules of a Pricelist

> **Module:** ssi_product
>
> **Extends:** `product` (Odoo core) — model `product.pricelist`
>
> **Model:** `product.pricelist`
>
> **Menu:** Product & Pricelist > Pricelist > Pricelists
>
> **Actor:** user in group _Pricelist_

This work instruction documents only what `ssi_product` adds to `product.pricelist`: the
**Price Rules** smart button (`action_view_price_rules`) and the rule counter it
displays. Everything else on this form is core Odoo behaviour and is not repeated here.

## Pre-Condition

- **Record:** The pricelist to inspect already exists.
- **Access:** User is in group _Pricelist_.
- **Module:** `ssi_product` is installed — without it the pricelist form has no button
  box and no **Price Rules** button.

## Flow

1. Open the **Product & Pricelist > Pricelist > Pricelists** menu. The pricelists are
   displayed as a list.
2. Open the pricelist whose price rules are to be inspected.
3. In the button box at the top of the form, read the **Price Rules** button. The number
   above its label is the count of price rules currently attached to this pricelist.
4. Click the **Price Rules** button (`action_view_price_rules`).

## Post-Condition

- The **Price Rules** list opens, restricted to the price rules of the pricelist the
  button was clicked from.
- A price rule created from this list is attached to that same pricelist by default.
- The search panel of that list additionally offers **Product**, **Product Template**,
  and **Product Category** as search fields — they are added by this module.
