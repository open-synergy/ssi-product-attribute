# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class ProductProduct(models.Model):
    """
    Adds brand-aware display names and category-based ordering.

    Reorders the default listing by category first, and overrides
    ``name_get`` so the product's brand is appended to its display
    name.
    """

    _inherit = "product.product"
    _order = "categ_id, sequence, default_code, name, id"

    def name_get(self):
        """Append the product brand to the standard display name.

        Overridden so that, when a product has
        ``product_brand_id`` set, the brand name is shown in
        parentheses after the name core Odoo would otherwise
        generate (``"<name> (<brand>)"``). Products without a
        brand keep core's unmodified result.

        :return: list of ``(id, display_name)`` tuples
        """
        res = super(ProductProduct, self).name_get()
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
