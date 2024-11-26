/** @odoo-module **/

import { patch } from '@web/core/utils/patch';
import { OrderReceipt } from "@point_of_sale/app/screens/receipt_screen/receipt/order_receipt";

patch(OrderReceipt.prototype, {
    setup() {
        super.setup();
        console.log("Custom OrderReceipt setup executed");
    },
}); 