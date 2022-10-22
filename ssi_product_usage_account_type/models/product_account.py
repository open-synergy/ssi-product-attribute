# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ProductAccount(models.Model):
    _name = "product.account"
    _description = "Product Accounts"

    product_id = fields.Many2one(
        string="Product",
        comodel_name="product.product",
        required=True,
        ondelete="cascade",
    )
    usage_id = fields.Many2one(
        string="Usage",
        comodel_name="product.usage_type",
        required=True,
        ondelete="restrict",
    )
    selection_method = fields.Selection(
        string="Selection Method",
        selection=[
            ("fixed", "Fixed"),
            ("python", "Python Code"),
        ],
        required=True,
        default="fixed",
    )
    account_id = fields.Many2one(
        string="Account",
        comodel_name="account.account",
        required=True,
        ondelete="restrict",
        company_dependent=True,
    )

    @api.constrains(
        "usage_id",
        "product_id",
    )
    def constrains_no_duplicate(self):
        for record in self:
            if not record._check_no_duplicate():
                error_message = _(
                    """
                Context: Add/Update product account configuration
                Database ID: %s
                Problem: Duplicate configuration
                Solution: Remove duplicate entry
                """
                    % (record.product_id.id)
                )
                raise ValidationError(error_message)

    def _check_no_duplicate(self):
        self.ensure_one()
        result = True
        ProductAccount = self.env["product.account"]
        criteria = [
            ("id", "!=", self.id),
            ("product_id", "=", self.product_id.id),
            ("usage_id", "=", self.usage_id.id),
        ]
        product_accounts = ProductAccount.search(criteria)
        if len(product_accounts) > 0:
            result = False
        return result