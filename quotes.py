from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database online config: https://api.elephantsql.com/console/f445e272-1613-4d69-a526-468bbca2cfe9/details?
# Tengo que crear una BD 'quotes' en el pgadmin, ver de hacer con docker-compose_bk.yml para trasladarla fácilmente
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:Admin123@localhost/quotes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Favquotes(db.Model):
    """ Modelado de la base de datos

    Attributes:
        id (int): id de la cita
        author (str): autor de la cita
        quote (str): cita
    """
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100))
    quote = db.Column(db.String(2000))


@app.route('/')
def index():
    """ Función encargada de renderizar el index.html """
    return render_template('index.html')


# Endpoints
@app.route('/quotes')
def quotes():
    return render_template('quotes.html')


@app.route('/process', methods=['POST'])
def process():
    author = request.form['author']
    quote = request.form['quote']
    return redirect(url_for('index'))


if __name__ == "__main__":

    app.run(debug=True)
