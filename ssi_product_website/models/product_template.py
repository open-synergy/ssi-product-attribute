from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from odoo.addons.http_routing.models.ir_http import slug


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def _compute_catalog_url(self):
        for product in self:
            if product.id:
                product.catalog_url = "/product_catalog/%s" % slug(product)

    catalog_url = fields.Char(
        string='Catalog URL',
        compute='_compute_catalog_url')
