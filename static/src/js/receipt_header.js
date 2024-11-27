/** @odoo-module **/

import { patch } from '@web/core/utils/patch';
import { ReceiptHeader } from "@point_of_sale/app/screens/receipt_screen/receipt/receipt_header/receipt_header";

console.log("Custom Receipt Header JS Loaded");

patch(ReceiptHeader.prototype, {
    setup() {
        super.setup();
        console.log("Custom ReceiptHeader setup executed");
        
        const company = this.props.data.company;
        console.log("Company Address Fields:", {
            street: company.street,
            street2: company.street2,
            city: company.city,
            state: company.state_id,
            country: company.country_id,
            phone: company.phone,
            email: company.email,
            website: company.website
        });
        
        const address = this.companyAddress;
        console.log("Formatted Company Address:", address);
    },

    get companyAddress() {
        const company = this.props.data.company;
        const address = [];

        // Add available address components
        if (company.street) address.push(company.street);
        if (company.street2) address.push(company.street2);
        if (company.city) address.push(company.city);
        if (company.state_id) address.push(company.state_id[1]); // state_id is [id, name]
        if (company.country_id) address.push(company.country_id[1]); // country_id is [id, name]

        return address.join(', ');
    }
});