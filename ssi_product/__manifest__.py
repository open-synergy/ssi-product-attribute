# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    "name": "Product App",
    "version": "14.0.1.3.2",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "LGPL-3",
    "installable": True,
    "application": True,
    "depends": [
        "product",
    ],
    "data": [
        "security/ir_module_category_data.xml",
        "security/res_group_data.xml",
        "security/ir.model.access.csv",
        "menu.xml",
        "views/uom_category_views.xml",
        "views/uom_uom_views.xml",
        "views/product_category_views.xml",
        "views/product_packaging_views.xml",
        "views/product_template_views.xml",
        "views/product_product_views.xml",
        "views/product_pricelist_views.xml",
        "views/product_attribute_views.xml",
        "views/product_supplierinfo_views.xml",
    ],
    "demo": [],
}
