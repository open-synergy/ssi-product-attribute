# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models

from odoo.addons.ssi_decorator import ssi_decorator


class MixinProductPricelistM2oConfigurator(models.AbstractModel):
    """
    Provide a configurable Many2one selection of ``product.pricelist``.

    Lets a host model restrict which ``product.pricelist`` records are
    selectable, either manually, by domain, or by Python code, and
    inject the corresponding form widget into the host view.
    """

    _name = "mixin.product_pricelist_m2o_configurator"
    _inherit = [
        "mixin.decorator",
    ]
    _description = "product.pricelist Many2one Configurator Mixin"

    _product_pricelist_m2o_configurator_insert_form_element_ok = False
    _product_pricelist_m2o_configurator_form_xpath = False

    pricelist_selection_method = fields.Selection(
        default="domain",
        selection=[("manual", "Manual"), ("domain", "Domain"), ("code", "Python Code")],
        string="Pricelist Selection Method",
        required=True,
    )
    pricelist_ids = fields.Many2many(
        comodel_name="product.pricelist",
        string="Pricelists",
    )
    pricelist_domain = fields.Text(default="[]", string="Pricelist Domain")
    pricelist_python_code = fields.Text(
        default="result = []", string="Pricelist Python Code"
    )

    @ssi_decorator.insert_on_form_view()
    def _product_pricelist_m2o_configurator_insert_form_element(self, view_arch):
        """Inject the pricelist configurator widget into the form.

        Hooked by ``ssi_decorator.insert_on_form_view`` so every host
        model gets the selection method, domain, and Python code fields
        spliced into its form view automatically.

        :param view_arch: current form view arch of the host model
        :return: ``view_arch`` with the configurator template inserted
            at ``_product_pricelist_m2o_configurator_form_xpath`` when
            ``_product_pricelist_m2o_configurator_insert_form_element_ok``
            is ``True``; unchanged otherwise
        """
        # TODO
        template_xml = "ssi_product."
        template_xml += "pricelist_m2o_configurator_template"
        if self._product_pricelist_m2o_configurator_insert_form_element_ok:
            view_arch = self._add_view_element(
                view_arch=view_arch,
                qweb_template_xml_id=template_xml,
                xpath=self._product_pricelist_m2o_configurator_form_xpath,
                position="inside",
            )
        return view_arch
