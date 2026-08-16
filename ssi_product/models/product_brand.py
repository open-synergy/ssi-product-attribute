# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ProductBrand(models.Model):
    """
    Represents a commercial brand that products can be tagged with.

    Extends ``mixin.master_data`` so brands follow the standard
    master data lifecycle (draft/valid/expired states, sequence,
    active flag). Products link back to their brand via
    ``product.template.product_brand_id``.
    """

    _name = "product.brand"
    _inherit = [
        "mixin.master_data",
    ]
    _description = "Product Brand"
    _order = "name"

    @api.depends("product_ids")
    def _compute_products_count(self):
        """Count the products currently tagged with this brand.

        :return: no return value; sets ``products_count`` on each
            record in ``self`` from the length of ``product_ids``
        """
        for rec in self:
            rec.products_count = len(rec.product_ids)

    partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Partner",
        help="Select a partner for this brand if it exists",
        ondelete="restrict",
    )
    logo = fields.Binary(string="Logo File")
    product_ids = fields.One2many(
        comodel_name="product.template",
        inverse_name="product_brand_id",
        string="Brand Products",
    )
    products_count = fields.Integer(
        string="Number of products",
        compute="_compute_products_count",
        compute_sudo=True,
    )
