# Final Salsabilah-Empire-OS Engine
from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>SR Electronics Park - Dashboard Online</h1><p>Authorized Dealer: Minister, MyOne, Butterfly Group</p>"

@app.route('/api/sync')
def sync_all_products():
    # এই ফাংশনটি ভবিষ্যতে ওয়েবসাইট থেকে সরাসরি ডাটা টানবে
    return jsonify({"status": "Success", "message": "Synced with Minister, MyOne & Butterfly Web Databases"})

if __name__ == "__main__":
    app.run(debug=True)
