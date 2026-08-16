# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import fields, models


class ProductCategory(models.Model):
    """
    Adds an explicit ordering field to ``product.category``.

    Core Odoo does not expose a manual ``sequence`` on product
    categories; this module adds one so categories can be ordered
    by the user instead of falling back to name/id ordering.
    """

    _name = "product.category"
    _inherit = "product.category"
    _order = "parent_id, sequence, id"

    sequence = fields.Integer(
        string="Sequence",
        default=4,
        required=True,
    )
