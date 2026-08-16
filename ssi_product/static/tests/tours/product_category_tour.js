odoo.define("ssi_product.product_category_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    // IK: docs/product_category/01-create.md
    //
    // Menu path in the IK is "Product & Pricelist > Configuration > Product
    // Categories & Attributes > Categories", but "Product Categories &
    // Attributes" (menu_category_root) sits at level 3 and has children of its
    // own, so 14.0 renders it as a non-clickable dropdown header without
    // [data-menu-xmlid] and flattens its children into the level-2
    // "Configuration" dropdown — there is no step for it (patterns.md
    // "Jumlah level menu di IK != jumlah step tour").
    //
    // The gate names the TARGET action ("Product Categories"); the app landing
    // action is "Products", which does not contain that string, so the gate
    // cannot pass on the previous screen.
    tour.register(
        "ssi_product_product_category_create",
        {
            test: true,
            url: "/web",
        },
        [
            // -- Flow 1 -- Open the Categories menu.
            tour.stepUtils.showAppsMenuItem(),
            {
                content: "Open the Product & Pricelist app",
                trigger: '.o_app[data-menu-xmlid="ssi_product.menu_root_product"]',
            },
            {
                content: "Open the Configuration menu",
                trigger:
                    ".o_menu_sections " +
                    '[data-menu-xmlid="ssi_product.menu_product_configuration"]',
            },
            {
                content: "Open the Categories menu",
                trigger:
                    ".o_menu_sections " +
                    '[data-menu-xmlid="ssi_product.product_category_menu"]',
            },
            {
                content: "Product Categories list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active" +
                    ":contains(Product Categories)",
                extra_trigger: ".o_list_view",
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

            // -- Flow 3 -- Fill in Category name and the Sequence field this
            // module adds.
            {
                content: "Fill in Category name",
                trigger: ".o_field_widget[name='name']",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text TOUR Category",
            },
            {
                content: "The Sequence field added by this module is displayed",
                // Anchor on the label, which always carries text; the input
                // itself would be an empty-looking box in readonly renders
                // (patterns.md section O).
                trigger: ".o_form_label:contains(Sequence)",
                extra_trigger: ".o_form_view.o_form_editable",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Fill in Sequence",
                trigger: ".o_field_widget[name='sequence']",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text 7",
            },

            // -- Flow 4 -- Click Save.
            {
                content: "Save the record",
                trigger: ".o_form_button_save",
            },

            // -- Post-Condition -- the category record exists. Its ordering is
            // a computed effect of the Sequence value, which is unit test
            // territory, so the tour stops at the saved record.
            {
                content: "Record is saved",
                trigger: ".o_form_view.o_form_readonly",
                extra_trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(TOUR Category)",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ]
    );
});
