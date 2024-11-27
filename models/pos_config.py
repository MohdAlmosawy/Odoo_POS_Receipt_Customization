from odoo import models

class PosConfig(models.Model):
    _inherit = 'pos.session'

    def _loader_params_res_company(self):
        result = super()._loader_params_res_company()
        result['search_params']['fields'].extend([
            'street',
            'street2',
            'city',
            'zip'
        ])
        return result 