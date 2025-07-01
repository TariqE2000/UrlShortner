from flask import Flask, request
from databaseConnection import get_db
from markupsafe import escape
from utility import shortenUrl


app = Flask(__name__)

# testing database 
@app.route('/test_db')
def test_db():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT 1;')
    result = cursor.fetchone()
    return f'Database is working! Result: {result[0]}', 200


@app.get('/shorten/<some_fucking_short_url>')
def original_url(some_fucking_short_url):
    original_fucking_url = f'www.{some_fucking_short_url}.com'
    return escape(original_fucking_url), 201

@app.post('/shorten')
def shorten_url():
    data = request.json
    return f'the long fucking url is {shortenUrl(data['url'])}'

