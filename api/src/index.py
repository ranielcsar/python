from src.routes.incomes import incomes_route
from src.routes.expenses import expenses_route
from src.model.income import Income
from src.model.expense import Expense
from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app, origins=r"/*")


transactions = [
    Income('Salary', 5000),
    Income('Dividends', 200),
    Expense('Pizza', 50),
    Expense('Rock Concert', 100)
]


incomes_route(app, transactions)
expenses_route(app, transactions)


if __name__ == "__main__":
    app.run()
