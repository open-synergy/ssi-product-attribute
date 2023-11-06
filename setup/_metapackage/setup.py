import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-open-synergy-ssi-product-attribute",
    description="Meta package for open-synergy-ssi-product-attribute Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-ssi_product',
        'odoo14-addon-ssi_product_purchase',
        'odoo14-addon-ssi_product_sale',
        'odoo14-addon-ssi_product_stock',
        'odoo14-addon-ssi_product_usage_account_type',
        'odoo14-addon-ssi_product_website',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
