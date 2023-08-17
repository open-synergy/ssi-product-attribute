odoo.define("ssi_product_website.tour_shop_frontend", function (require) {
"use strict";

var tour = require("web_tour.tour");
var steps = require("ssi_product_website.tour_shop");
tour.register("product_catalog", {
    url: "/product_catalog",
    sequence: 130,
}, steps);

});
