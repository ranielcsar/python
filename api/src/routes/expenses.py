from src.model.expense import Expense, ExpenseSchema
from src.model.transaction_type import TransactionType
from flask import jsonify, request


def expenses_route(app, transactions):
    @app.route('/expenses')
    def get_expenses():
        schema = ExpenseSchema(many=True)
        expenses = schema.dump(
            filter(lambda transaction: transaction.type ==
                   TransactionType.EXPENSE, transactions)
        )

        return jsonify(expenses)

    @app.route('/expenses', methods=['POST'])
    def add_expense():
        expense = ExpenseSchema().load(request.get_json())
        transactions.append(expense)

        return "", 204
