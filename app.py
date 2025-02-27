from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
DB_NAME = "quotes.db"
CORS(app)
def get_random_quote():
    '''Get a random quote from the database'''
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()


    cursor.execute("SELECT driver, quote FROM quotes ORDER BY RANDOM() LIMIT 1")
    driver, quote = cursor.fetchone()
    conn.close()
    return {"driver": driver, "quote": quote}


@app.route("/quote", methods=["GET"])
def random_quote():
    '''API endpoint to return a random quote'''
    return jsonify(get_random_quote())

if __name__ == "__main__":
    app.run(debug=True)

