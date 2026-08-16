# Delete Product Brand

> **Module:** ssi_product
>
> **Model:** `product.brand`
>
> **Menu:** Product & Pricelist > Configuration > Product Categories & Attributes >
> Product Brands
>
> **Actor:** user in group _Product Brand_
>
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The brand to delete already exists.
- **Record:** No product template still refers to this brand — the **Products** smart
  button shows **0**.
- **Access:** User is in group _Product Brand_.

## Flow

1. Open the **Product & Pricelist > Configuration > Product Categories & Attributes >
   Product Brands** menu.
2. Open the brand card to delete.
3. Click **Action** > **Delete**.
4. Click **OK** to confirm.
5. Click the **Brand** breadcrumb link to return to the kanban view.

## Post-Condition

- The brand is permanently removed from the system.
- The deleted brand no longer appears in the **Product Brands** kanban view.
- The brand is no longer selectable as **Brand** on product templates.
