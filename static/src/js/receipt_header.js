/** @odoo-module **/

import { patch } from '@web/core/utils/patch';
import { ReceiptHeader } from "@point_of_sale/app/screens/receipt_screen/receipt/receipt_header/receipt_header";

console.log("Custom Receipt Header JS Loaded");

patch(ReceiptHeader.prototype, {
    setup() {
        super.setup();
        console.log("Custom ReceiptHeader setup executed");
    },
});