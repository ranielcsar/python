# from src.routes.incomes import add_income, get_incomes
from src.model.transaction_type import TransactionType
from src.model.income import Income, IncomeSchema
from src.model.expense import Expense, ExpenseSchema
from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app, origins=r"/*")


transactions = [
    Income('Salary', 5000),
    Income('Dividends', 200),
    Expense('Pizza', 50),
    Expense('Rock Concert', 100)
]


@app.route('/incomes')
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


if __name__ == "__main__":
    app.run()
