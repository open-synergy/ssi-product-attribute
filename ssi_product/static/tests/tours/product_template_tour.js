odoo.define("ssi_product.product_template_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    // IK: docs/product_template/01-create.md
    //
    // "Products" (product_template_menu) is a level-2 leaf menu, so it keeps
    // its [data-menu-xmlid] and is a step of its own. It is also the landing
    // action of the app, so the breadcrumb gate below is satisfied by the very
    // action the step opens — there is no earlier screen it could match by
    // mistake.
    tour.register(
        "ssi_product_product_template_create",
        {
            test: true,
            url: "/web",
        },
        [
            // -- Flow 1 -- Open the Products menu; the list carries the Brand
            // column added by this module.
            tour.stepUtils.showAppsMenuItem(),
            {
                content: "Open the Product & Pricelist app",
                trigger: '.o_app[data-menu-xmlid="ssi_product.menu_root_product"]',
            },
            {
                content: "Open the Products menu",
                trigger:
                    ".o_menu_sections " +
                    '[data-menu-xmlid="ssi_product.product_template_menu"]',
            },
            {
                content: "Products list is displayed",
                trigger: ".o_control_panel .breadcrumb-item.active:contains(Products)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "The Brand column added by this module is displayed",
                trigger: ".o_list_view th:contains(Brand)",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },

            // -- Flow 2 -- Click the New button. (14.0: "Create")
            {
                content: "Click Create",
                trigger: ".o_list_button_add",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Form is open in edit mode",
                trigger: ".o_form_view.o_form_editable",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },

            // -- Flow 3 -- Fill in Product Name, then the Brand and Sequence
            // fields this module adds to the General Information tab.
            {
                content: "Fill in Product Name",
                trigger: ".o_field_widget[name='name']",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text TOUR Product Template",
            },
            {
                content: "Type the brand name",
                trigger: ".o_field_many2one[name='product_brand_id'] input",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text TOUR Brand Template",
            },
            {
                content: "Pick the brand from the dropdown",
                trigger:
                    ".ui-autocomplete .ui-menu-item a:contains(TOUR Brand Template)",
                in_modal: false,
            },
            {
                content: "Fill in Sequence",
                trigger: ".o_field_widget[name='sequence']",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text 5",
            },

            // -- Flow 4 -- Click Save.
            {
                content: "Save the record",
                trigger: ".o_form_button_save",
            },

            // -- Post-Condition -- the product is saved and its Brand is shown
            // on the form. Whether the brand is appended to the display name is
            // a value, hence unit test territory, not a tour assertion.
            {
                content: "Record is saved and shows the Brand field",
                trigger: ".o_form_view.o_form_readonly .o_form_label:contains(Brand)",
                extra_trigger:
                    ".o_control_panel .breadcrumb-item.active" +
                    ":contains(TOUR Product Template)",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ]
    );
});
