/** @odoo-module **/

import { patch } from '@web/core/utils/patch';
import { Orderline } from "@point_of_sale/app/generic_components/orderline/orderline";

patch(Orderline.prototype, {
    setup() {
        super.setup();
        console.log("Orderline setup called - this:", this);
    },
    
    get orderlineClasses() {
        const classes = super.orderlineClasses;
        console.log("Orderline classes:", classes);
        return classes;
    }
});
