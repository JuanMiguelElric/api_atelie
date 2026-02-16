from database.database import get_driver
from repository.Cliente_Repository import Cliente_Repository
from flask import request, jsonify

class ClienteController:

    @staticmethod
    def create_post():
        try:
            with get_driver() as driver:

                cliente = request.form.get('cliente')
                costureira = request.form.get('costureira')
                medida = request.form.get('medida')
                roupa = request.form.get('roupa')
                valor = request.form.get('valor')

                if not cliente or not costureira or not medida or not roupa or not valor:
                    return jsonify({"error": "Campos vazios"}), 400

                Cliente_Repository.save(
                    driver,
                    cliente,
                    costureira,
                    medida,
                    roupa,
                    valor
                )

                return jsonify({"message": "Cliente salvo com sucesso"}), 201

        except Exception as e:
            return jsonify({"error": str(e)}), 500
