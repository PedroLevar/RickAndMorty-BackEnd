from flask import jsonify

class ApiResponse:
    @staticmethod
    def response(success=True, message="Success", data=None, status_code=200):
        """
        Retorna uma resposta padronizada.
        """
        response = {
            "success": success,
            "message": message,
            "data": data
        }
        return jsonify(response), status_code