from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/')
def home():
    return "Salsabilah Empire OS is Live at SR Electronics Park!"

@app.route('/api/stock')
def stock():
    with open('inventory_db.json', 'r') as f:
        return jsonify(json.load(f))

if __name__ == "__main__":
    app.run(debug=True)
