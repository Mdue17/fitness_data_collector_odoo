import json
from odoo import http
from odoo.http import request

class FitnessApi(http.Controller):
    @http.route('/fitness/api/session', auth='public', type='json', csrf=False, methods=['POST'])
    def create_session(self, **data):
        # Get the data from the incoming JSON request
        # data = request.jsonrequest

        try:
            # Create the fitness session record
            session = request.env['fitness.session'].sudo().create(data)
            return {"status": "success", "id": session.id}
        except Exception as e:
            # Handle errors and send an error message
            return {"status": "error", "message": str(e)}