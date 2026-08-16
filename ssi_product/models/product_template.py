# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProductTemplate(models.Model):
    """
    Adds a brand field and brand-aware display names to templates.

    Lets each product template be tagged with a ``product.brand``,
    and overrides ``name_get`` so the brand is appended to the
    template's display name.
    """

    _inherit = "product.template"

    product_brand_id = fields.Many2one(
        comodel_name="product.brand",
        string="Brand",
        help="Select a brand for this product",
    )

    def name_get(self):
        """Append the product brand to the standard display name.

        Overridden so that, when a template has
        ``product_brand_id`` set, the brand name is shown in
        parentheses after the name core Odoo would otherwise
        generate (``"<name> (<brand>)"``). Templates without a
        brand keep core's unmodified result.

        :return: list of ``(id, display_name)`` tuples
        """
        res = super(ProductTemplate, self).name_get()
        res2 = []
        for name_tuple in res:
            product = self.browse(name_tuple[0])
            if not product.product_brand_id:
                res2.append(name_tuple)
                continue
            res2.append(
                (
                    name_tuple[0],
                    "{} ({})".format(name_tuple[1], product.product_brand_id.name),
                )
            )
        return res2
