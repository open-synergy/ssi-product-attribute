# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# HttpSavepointCase — NOT HttpCase. 14.0's HttpCase has no cls.env in
# setUpClass (see odoo-development-ui-test skill, structure-and-runner.md).
from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiProductCategory(HttpSavepointCase):
    """Tour test for the ``product.category`` work instruction."""

    def test_create(self):
        """Run the create tour for ``product.category``.

        The tour needs no fixture: it creates the category through the UI,
        and the only surface this module adds to the model is the
        ``sequence`` field on that same form.

        ``ssi_product.product_category_group`` already grants
        ``base.user_root`` and ``base.user_admin`` membership in
        ``security/res_group_data.xml``, so ``admin`` reaches the
        Categories menu without any extra group setup.

        IK: docs/product_category/01-create.md
        """
        self.start_tour("/web", "ssi_product_product_category_create", login="admin")
