odoo.define("ssi_product.product_pricelist_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    // IK: docs/product_pricelist/04-view-price-rules.md
    //
    // "Pricelist" (menu_pricelist_root) has children but sits at level 2, so
    // 14.0 renders it as a clickable dropdown toggle that keeps its
    // [data-menu-xmlid] — unlike a level-3 grouping menu, it IS a step. Its
    // child "Pricelists" (product_pricelist_menu) is a leaf and is the next
    // step.
    //
    // action_view_price_rules is type="object", so button[name='...'] matches
    // it (selectors.md section 4); the numeric-id caveat only applies to
    // type="action" buttons.
    tour.register(
        "ssi_product_product_pricelist_view_price_rules",
        {
            test: true,
            url: "/web",
        },
        [
            // -- Flow 1 -- Open the Pricelists menu.
            tour.stepUtils.showAppsMenuItem(),
            {
                content: "Open the Product & Pricelist app",
                trigger: '.o_app[data-menu-xmlid="ssi_product.menu_root_product"]',
            },
            {
                content: "Open the Pricelist menu",
                trigger:
                    ".o_menu_sections " +
                    '[data-menu-xmlid="ssi_product.menu_pricelist_root"]',
            },
            {
                content: "Open the Pricelists menu",
                trigger:
                    ".o_menu_sections " +
                    '[data-menu-xmlid="ssi_product.product_pricelist_menu"]',
            },
            {
                content: "Pricelists list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Pricelists)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },

            // -- Flow 2 -- Open the pricelist to inspect.
            {
                content: "Open the pricelist",
                trigger: ".o_data_row:contains(TOUR Pricelist) .o_data_cell:first",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Pricelist form is open",
                trigger: ".o_form_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },

            // -- Flow 3 -- Read the Price Rules button in the button box. Its
            // label is always rendered, so it is a safe anchor; the counter
            // above it is a computed value and belongs to the unit test.
            {
                content: "The Price Rules button added by this module is displayed",
                trigger:
                    "button[name='action_view_price_rules'] " +
                    ".o_stat_text:contains(Price Rules)",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },

            // -- Flow 4 -- Click the Price Rules button.
            {
                content: "Click the Price Rules button",
                trigger: "button[name='action_view_price_rules']",
                extra_trigger: ".o_form_view",
            },

            // -- Post-Condition -- the Price Rules list opens. The gate names
            // the target action: before the click the active breadcrumb is the
            // pricelist name, so it cannot match by mistake.
            {
                content: "Price Rules list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Price Rules)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ]
    );
});
