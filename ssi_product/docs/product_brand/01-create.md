# Create Product Brand

> **Module:** ssi_product
>
> **Model:** `product.brand`
>
> **Menu:** Product & Pricelist > Configuration > Product Categories & Attributes >
> Product Brands
>
> **Actor:** user in group _Product Brand_
>
> **Inline Actions:** `action_generate_code` (Generate Code)

## Pre-Condition

- **Access:** User is in group _Product Brand_.
- **Config:** An active `sequence.template` for `product.brand` exists if the code is to
  be assigned automatically by **Generate Code**. Without it the code has to be typed by
  hand.

## Flow

1. Open the **Product & Pricelist > Configuration > Product Categories & Attributes >
   Product Brands** menu. The brands are displayed as kanban cards.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Name** _(required)_: Enter the brand name as it should appear on products.
   - **Code** _(required)_: Enter a unique code for this brand, or enter **/** to leave
     it eligible for automatic assignment via **Generate Code**.
   - **Logo File** (on the **Image** tab): Optional. Upload the image shown on the brand
     kanban card.
4. Open the **Note** tab and fill in **Note** with a short description of the brand. The
   kanban card shows the first 200 characters of this text.
5. In the header, click **Generate Code** to assign a code from the sequence configured
   by an active `sequence.template` for this model. Only applies while **Code** is still
   **/**; otherwise the code stays exactly as typed.
6. No `sequence.template` is currently configured for **Product Brand**, so a warning
   dialog appears instead of a new code being assigned. Click **OK** to dismiss it.
   **Code** remains **/**.
7. Click **Save**.

## Post-Condition

- A new product brand record is created and active.
- The new brand appears in the **Product Brands** kanban view.
- The brand becomes selectable as **Brand** on product templates and their variants.

## Related Views

- The **Products** smart button in the button box opens the list of product templates
  that carry this brand. It only navigates — it changes nothing on the brand itself.
