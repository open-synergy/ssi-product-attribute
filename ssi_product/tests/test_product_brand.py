# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestProductBrand(YamlTransactionCase):
    """Test ``product.brand`` creation, linking, and computed fields."""

    def test_product_brand(self):
        """Run the product brand scenario.

        Covers brand creation, linking a brand to a product template
        and its variant, product category sequence, and the computed
        ``products_count`` field.
        """
        self.run_yaml_scenario("test_data_product_brand.yaml")
