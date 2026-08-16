# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# HttpSavepointCase — NOT HttpCase. 14.0's HttpCase has no cls.env in
# setUpClass (see odoo-development-ui-test skill, structure-and-runner.md).
from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiProductPricelist(HttpSavepointCase):
    """Tour test for the ``product.pricelist`` work instruction."""

    @classmethod
    def setUpClass(cls):
        """Create the pricelist the tour opens, with one price rule.

        The rule exists so the Price Rules button reports a non-empty
        list; its value is never asserted by the tour.

        ``ssi_product.pricelist_configurator_group`` already grants
        ``base.user_root`` and ``base.user_admin`` membership in
        ``security/res_group_data.xml``, so ``admin`` reaches the
        Pricelists menu without any extra group setup.
        """
        super().setUpClass()
        cls.pricelist = cls.env["product.pricelist"].create(
            {
                "name": "TOUR Pricelist",
                "item_ids": [
                    (
                        0,
                        0,
                        {
                            "applied_on": "3_global",
                            "compute_price": "fixed",
                            "fixed_price": 100.0,
                        },
                    )
                ],
            }
        )

    def test_view_price_rules(self):
        """Run the price rules tour for ``product.pricelist``.

        The tour stops at the Price Rules list the button opens: which
        rules that list holds is a value, so it stays in the unit tests.

        IK: docs/product_pricelist/04-view-price-rules.md
        """
        self.start_tour(
            "/web", "ssi_product_product_pricelist_view_price_rules", login="admin"
        )
