# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# HttpSavepointCase — NOT HttpCase. 14.0's HttpCase has no cls.env in
# setUpClass (see odoo-development-ui-test skill, structure-and-runner.md).
from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiProductBrand(HttpSavepointCase):
    """Tour tests for the ``product.brand`` work instructions."""

    @classmethod
    def setUpClass(cls):
        """Create the ``product.brand`` fixtures each tour needs.

        ``ssi_product.product_brand_group`` already grants
        ``base.user_root`` and ``base.user_admin`` membership in
        ``security/res_group_data.xml``, so ``admin`` reaches the Product
        Brands menu without any extra group setup.

        ``note`` is filled deliberately: the brand kanban card renders
        ``record.note.value.substr(0, 200)``, and 14.0 leaves
        ``record.note.value`` undefined when the field is empty, which
        breaks the kanban template the tours navigate through.
        """
        super().setUpClass()
        cls.brand_edit = cls.env["product.brand"].create(
            {
                "name": "TOUR Brand Edit",
                "code": "/",
                "note": "Tour fixture for the edit work instruction.",
            }
        )
        cls.brand_delete = cls.env["product.brand"].create(
            {
                "name": "TOUR Brand Delete",
                "code": "/",
                "note": "Tour fixture for the delete work instruction.",
            }
        )

    def test_create(self):
        """Run the create tour for ``product.brand``.

        The optional Logo File on the Image tab is asserted by neither the
        tour nor this test: uploading a real file through a hidden
        ``<input type="file">`` has no reliable DOM completion signal.

        IK: docs/product_brand/01-create.md
        """
        self.start_tour("/web", "ssi_product_product_brand_create", login="admin")

    def test_edit(self):
        """Run the edit tour for ``product.brand``.

        IK: docs/product_brand/02-edit.md
        """
        self.start_tour("/web", "ssi_product_product_brand_edit", login="admin")

    def test_delete(self):
        """Run the delete tour for ``product.brand``.

        IK: docs/product_brand/03-delete.md
        """
        self.start_tour("/web", "ssi_product_product_brand_delete", login="admin")
