# Edit Product Brand

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
>
> **Inline Actions:** `action_generate_code` (Generate Code)

## Pre-Condition

- **Record:** The brand to edit already exists.
- **Access:** User is in group _Product Brand_.
- **Config:** An active `sequence.template` for `product.brand` exists if **Generate
  Code** is to assign a code. Without it the code has to be typed by hand.

## Flow

1. Open the **Product & Pricelist > Configuration > Product Categories & Attributes >
   Product Brands** menu.
2. Find and open the brand card to edit.
3. Click the **Edit** button.
4. Change **Name**, **Code**, **Active**, **Logo File**, or **Note** as needed.
5. In the header, click **Generate Code** to assign a code from the sequence configured
   by an active `sequence.template` for this model — for example after setting **Code**
   back to **/**. Only applies while **Code** is **/**.
6. No `sequence.template` is currently configured for **Product Brand**, so a warning
   dialog appears instead of a new code being assigned. Click **OK** to dismiss it.
   **Code** is left unchanged.
7. Click **Save**.

## Post-Condition

- The brand is updated with the new values.
- The updated brand appears with its new name in the **Product Brands** kanban view.

## Related Views

- The **Products** smart button in the button box opens the list of product templates
  that carry this brand. It only navigates — it changes nothing on the brand itself.
