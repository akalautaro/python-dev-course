from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database online config: https://api.elephantsql.com/console/f445e272-1613-4d69-a526-468bbca2cfe9/details?
# Tengo que crear una BD 'quotes' en el pgadmin, ver de hacer con docker-compose_bk.yml para trasladarla fácilmente
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:Admin123@localhost:5455/quotes_db'  # database en docker
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://fynuufotjfkcta:326854de53c459c009ba2c750bd82c16aca17e06a93b2b1e80679b102374609b@ec2-34-197-84-74.compute-1.amazonaws.com:5432/d7683i3jc4atns'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Quotes(db.Model):
    """ Modelado de la base de datos. Para ejecutarla debería ejecutar un python con:
    from quotes import db
    db.create_all()

    o con flask_migrate. En mi caso la cree en Docker con el script init.sql y docker-compose
    """
    quote_id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100))
    quote = db.Column(db.String(2000))


@app.route('/')
def index():
    """ Función encargada de renderizar el index.html """
    result = Quotes.query.order_by(Quotes.quote_id.desc()).all()
    return render_template('index.html', result=result)


# Endpoints
@app.route('/quotes')
def quotes():
    return render_template('quotes.html')


@app.route('/process', methods=['POST'])
def process():
    author = request.form['author']
    quote = request.form['quote']
    quotedata = Quotes(author=author, quote=quote)
    db.session.add(quotedata)
    db.session.commit()

    return redirect(url_for('index'))


if __name__ == "__main__":

    app.run(debug=True)
