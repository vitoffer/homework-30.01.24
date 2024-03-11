from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trading.db?charset=utf8'
app.config['JSON_AS_ASCII'] = False
db = SQLAlchemy(app)


class Market(db.Model):
    __tablename__ = 'Магазин'
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.String(100), nullable=False)


class Good(db.Model):
    __tablename__ = 'Товар'
    id = db.Column(db.Integer, primary_key=True)
    market_section = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    unit = db.Column(db.String(100), nullable=False)
    number_in_package = db.Column(db.String(100), nullable=False)
    provider = db.Column(db.String(100), nullable=False)

class Transaction(db.Model):
    __tablename__ = 'Торговля'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    market_id = db.Column(db.String(100), nullable=False)
    good_id = db.Column(db.Integer, nullable=False)
    operation = db.Column(db.String(100), nullable=False)
    package_count = db.Column(db.Integer, nullable=False)
    cost = db.Column(db.Integer, nullable=False)



@app.route('/markets')
def get_markets():
    markets = Market.query.all()
    market_list = [str({'id': market.id, 'area': market.area}) for market in markets]

    print(market_list)
    print()
    return '<br>'.join(market_list)


@app.route('/goods')
def get_transactions():
    goods = Good.query.all()
    good_list = [str({'id': good.id, 'section': good.market_section , 'name': good.name, 'unit': good.unit, 'count': good.number_in_package, 'provider': good.provider}) for good in goods]

    print(good_list)
    print()
    return '<br>'.join(good_list)

@app.route('/transactions')
def get_products():
    transactions = Transaction.query.all()
    transaction_list = [str({'id': transaction.id, 'date': transaction.date.strftime('%d.%m.%Y'), 'market_id': transaction.market_id, 'good_id': transaction.good_id, 'operation': transaction.operation, 'count': transaction.package_count, 'cost': transaction.cost}) for transaction in transactions]

    print(transaction_list)
    print()
    return '<br>'.join(transaction_list)


if __name__ == '__main__':
    app.run()
