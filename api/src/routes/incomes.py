from src.model.income import Income, IncomeSchema
from src.model.transaction_type import TransactionType
from flask import jsonify, request


def incomes_route(app, transactions):
    @app.route('/incomes', methods=['GET'])
    def get_incomes():
        schema = IncomeSchema(many=True)
        incomes = schema.dump(
            filter(lambda transaction: transaction.type ==
                   TransactionType.INCOME, transactions)
        )

        return jsonify(incomes)

    @app.route('/incomes', methods=['POST'])
    def add_income():
        income = IncomeSchema().load(request.get_json())
        transactions.append(income)

        return jsonify({'message': 'Income added succesfully'}), 200
