# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import ast

from odoo import api, fields, models


class ProductPricelist(models.Model):
    """
    Adds a price rule counter and smart-button action to pricelists.

    Lets users see, from the pricelist form, how many pricelist
    items (price rules) exist and jump straight to them filtered by
    the current pricelist.
    """

    _inherit = "product.pricelist"

    @api.depends("item_ids")
    def _compute_item_count(self):
        """Count the pricelist items attached to this pricelist.

        :return: no return value; sets ``item_count`` on each record
            in ``self`` from the length of ``item_ids``
        """
        for rec in self:
            rec.item_count = len(rec.item_ids)

    item_count = fields.Integer(
        string="Item Count", compute="_compute_item_count", compute_sudo=True
    )

    def action_view_price_rules(self):
        """Open the price rules (pricelist items) of this pricelist.

        Returns the standard ``product.product_pricelist_item_action``
        act_window, with its domain narrowed to
        ``pricelist_id = self.id`` and ``default_pricelist_id`` added
        to the context so new rules are created for this pricelist.

        :return: dict, the act_window action to display
        """
        self.ensure_one()
        action = self.env.ref("product.product_pricelist_item_action").read()[0]
        action["domain"] = [("pricelist_id", "=", self.id)]
        context = action.get("context", {})
        if isinstance(context, str):
            context = ast.literal_eval(context)
        context.update(
            {
                "default_pricelist_id": self.id,
            }
        )
        action["context"] = context
        return action
