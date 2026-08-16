odoo.define("ssi_product.product_brand_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    // Shared opening steps for every IK in this file: "Product & Pricelist >
    // Configuration > Product Categories & Attributes > Product Brands".
    // "Product Categories & Attributes" (menu_category_root) sits at level 3
    // and has children of its own, so 14.0 renders it as a non-clickable
    // dropdown header without [data-menu-xmlid] and flattens its children
    // into the level-2 "Configuration" dropdown — there is no step for it
    // (patterns.md "Jumlah level menu di IK != jumlah step tour").
    //
    // The gate names the TARGET action ("Brand"); the app landing action is
    // "Products", which does not contain "Brand", so there is no substring
    // clash. action_product_brand opens in KANBAN mode (view_mode
    // "kanban,tree,form"), hence .o_kanban_view rather than .o_list_view.
    function openProductBrandMenuSteps() {
        return [
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
                content: "Open the Product Brands menu",
                trigger:
                    ".o_menu_sections " +
                    '[data-menu-xmlid="ssi_product.menu_product_brand"]',
            },
            {
                content: "Product Brands kanban is displayed",
                trigger: ".o_control_panel .breadcrumb-item.active:contains(Brand)",
                extra_trigger: ".o_kanban_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ];
    }

    // IK: docs/product_brand/01-create.md
    tour.register(
        "ssi_product_product_brand_create",
        {
            test: true,
            url: "/web",
        },
        [].concat(openProductBrandMenuSteps(), [
            // -- Flow 2 -- Click the New button. (14.0: "Create")
            {
                content: "Click Create",
                trigger: ".o-kanban-button-new",
                extra_trigger: ".o_kanban_view",
            },
            {
                content: "Form is open in edit mode",
                trigger: ".o_form_view.o_form_editable",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },

            // -- Flow 3 -- Fill in the required fields. The optional Logo File
            // on the Image tab is skipped: uploading a real file through a
            // hidden <input type="file"> is not reliable in a tour
            // (patterns.md section Q).
            {
                content: "Fill in Name",
                trigger: ".o_field_widget[name='name']",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text TOUR Brand Create",
            },
            {
                content: "Fill in Code",
                trigger: ".o_field_widget[name='code']",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text /",
            },

            // -- Flow 4 -- Open the Note tab and fill in Note.
            {
                content: "Open the Note tab",
                trigger: ".o_notebook .nav-link:contains(Note)",
                extra_trigger: ".o_form_view.o_form_editable",
            },
            {
                content: "Fill in Note",
                trigger: ".o_field_widget[name='note']",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text TOUR Brand Create note.",
            },

            // -- Flow 5 -- Click Generate Code in the header.
            {
                content: "Click Generate Code",
                trigger: ".o_statusbar_buttons button[name='action_generate_code']",
                extra_trigger: ".o_form_view",
            },

            // -- Flow 6 -- No sequence.template is configured for product.brand,
            // so a warning dialog appears instead of a new code. Click OK.
            {
                content: "Dismiss the missing sequence.template warning",
                trigger: ".modal-footer button.btn-primary",
                in_modal: true,
            },

            // -- Flow 7 -- Click Save.
            {
                content: "Save the record",
                trigger: ".o_form_button_save",
                extra_trigger: "body:not(:has(.modal))",
            },
            {
                content: "Record is saved",
                trigger: ".o_form_view.o_form_readonly",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },

            // -- Post-Condition -- the new brand appears in the kanban view.
            {
                content: "Click the Brand breadcrumb to go back to the kanban",
                trigger: ".breadcrumb-item.o_back_button a:contains(Brand)",
            },
            {
                content: "New brand is displayed in the kanban view",
                trigger: ".o_kanban_record:contains(TOUR Brand Create)",
                extra_trigger: ".o_kanban_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ])
    );

    // IK: docs/product_brand/02-edit.md
    tour.register(
        "ssi_product_product_brand_edit",
        {
            test: true,
            url: "/web",
        },
        [].concat(openProductBrandMenuSteps(), [
            // -- Flow 2 -- Find and open the brand card to edit.
            {
                content: "Open the brand card",
                trigger: ".o_kanban_record:contains(TOUR Brand Edit)",
                extra_trigger: ".o_kanban_view",
            },
            {
                content: "Form is open",
                trigger: ".o_form_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },

            // -- Flow 3 -- Click the Edit button.
            {
                content: "Click the Edit button",
                trigger: ".o_form_button_edit",
            },
            {
                content: "Form is now editable",
                trigger: ".o_form_view.o_form_editable",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },

            // -- Flow 4 -- Change Name.
            {
                content: "Change the Name",
                trigger: ".o_field_widget[name='name']",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text TOUR Brand Edited",
            },

            // -- Flow 5 -- Click Generate Code in the header.
            {
                content: "Click Generate Code",
                trigger: ".o_statusbar_buttons button[name='action_generate_code']",
                extra_trigger: ".o_form_view",
            },

            // -- Flow 6 -- No sequence.template is configured for product.brand,
            // so a warning dialog appears instead of a new code. Click OK.
            {
                content: "Dismiss the missing sequence.template warning",
                trigger: ".modal-footer button.btn-primary",
                in_modal: true,
            },

            // -- Flow 7 -- Click Save.
            {
                content: "Save the record",
                trigger: ".o_form_button_save",
                extra_trigger: "body:not(:has(.modal))",
            },
            {
                content: "Record is saved",
                trigger: ".o_form_view.o_form_readonly",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },

            // -- Post-Condition -- the updated brand appears in the kanban view.
            {
                content: "Click the Brand breadcrumb to go back to the kanban",
                trigger: ".breadcrumb-item.o_back_button a:contains(Brand)",
            },
            {
                content: "Updated brand is displayed in the kanban view",
                trigger: ".o_kanban_record:contains(TOUR Brand Edited)",
                extra_trigger: ".o_kanban_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ])
    );

    // IK: docs/product_brand/03-delete.md
    tour.register(
        "ssi_product_product_brand_delete",
        {
            test: true,
            url: "/web",
        },
        [].concat(openProductBrandMenuSteps(), [
            // -- Flow 2 -- Open the brand card to delete.
            {
                content: "Open the brand card",
                trigger: ".o_kanban_record:contains(TOUR Brand Delete)",
                extra_trigger: ".o_kanban_view",
            },
            {
                content: "Form is open",
                trigger: ".o_form_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },

            // -- Flow 3 -- Click Action > Delete.
            {
                content: "Open the Action menu",
                trigger: ".o_cp_action_menus button:contains(Action)",
            },
            {
                content: "Click Delete",
                // Action menu items are Owl components; match the exact label
                // so ":contains(Delete)" never picks "Archive" instead.
                trigger: ".o_cp_action_menus .o_menu_item a",
                run: function () {
                    var $delete = $(".o_cp_action_menus .o_menu_item a").filter(
                        function () {
                            return $(this).text().trim() === "Delete";
                        }
                    );
                    $delete[0].click();
                },
            },

            // -- Flow 4 -- Click OK to confirm.
            {
                content: "Confirm deletion",
                trigger: ".modal-footer button.btn-primary",
                in_modal: true,
            },

            // -- Flow 5 -- Click the Brand breadcrumb to return to the kanban.
            {
                content: "Click the Brand breadcrumb",
                trigger: ".breadcrumb-item.o_back_button a:contains(Brand)",
                extra_trigger: "body:not(:has(.modal))",
            },

            // -- Post-Condition -- the deleted brand no longer appears.
            {
                content: "Deleted brand no longer appears in the kanban view",
                trigger:
                    ".o_kanban_view:not(:has(.o_kanban_record:contains(TOUR Brand Delete)))",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ])
    );
});
