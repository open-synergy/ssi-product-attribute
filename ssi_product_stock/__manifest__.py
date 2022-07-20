# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    "name": "Product App - stock Integration",
    "version": "14.0.1.0.0",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "LGPL-3",
    "installable": True,
    "application": False,
    "auto_install": True,
    "depends": [
        "ssi_product",
        "stock",
    ],
    "data": [
        # "security/ir_module_category_data.xml",
        # "security/res_group_data.xml",
        # "security/ir.model.access.csv",
        "menu.xml",
    ],
    "demo": [],
}
