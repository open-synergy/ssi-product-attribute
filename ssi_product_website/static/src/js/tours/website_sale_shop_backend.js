odoo.define("ssi_product_website.tour_shop_backend", function (require) {
"use strict";

var tour = require("web_tour.tour");
var steps = require("ssi_product_website.tour_shop");
tour.register("shop", {url: "/shop"}, steps);

});
