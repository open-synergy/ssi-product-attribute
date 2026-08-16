# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# HttpSavepointCase — NOT HttpCase. 14.0's HttpCase has no cls.env in
# setUpClass (see odoo-development-ui-test skill, structure-and-runner.md).
from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiProductProduct(HttpSavepointCase):
    """Tour test for the ``product.product`` work instruction."""

    @classmethod
    def setUpClass(cls):
        """Create the brand the create tour selects on the variant form.

        ``ssi_product.product_configurator_group`` already grants
        ``base.user_root`` and ``base.user_admin`` membership in
        ``security/res_group_data.xml``, so ``admin`` reaches the Product
        Varians menu without any extra group setup.

        ``note`` is filled deliberately: the brand kanban card renders
        ``record.note.value.substr(0, 200)``, and 14.0 leaves
        ``record.note.value`` undefined when the field is empty.
        """
        super().setUpClass()
        cls.brand = cls.env["product.brand"].create(
            {
                "name": "TOUR Brand Variant",
                "code": "/",
                "note": "Tour fixture for the product variant work instruction.",
            }
        )

    def test_create(self):
        """Run the create tour for ``product.product``.

        The tour asserts the Brand column, the Brand field, and the
        Sequence field this module adds to the variant surfaces. The
        resulting record order and the display name built by ``name_get``
        are values, so they stay in the unit tests.

        IK: docs/product_product/01-create.md
        """
        self.start_tour("/web", "ssi_product_product_product_create", login="admin")
