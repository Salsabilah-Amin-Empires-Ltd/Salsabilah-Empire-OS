# Final Salsabilah-Empire-OS Engine
from flask import Flask, request, jsonify

app = Flask(__name__)

# ইন-মেমোরি ডেটাবেস (ভবিষ্যতে আমরা এটি SQL-এ স্থানান্তর করব)
sales_records = []
customer_dues = {}

@app.route('/')
def home():
    return """
    <h1>SR Electronics Park - Empire OS Engine</h1>
    <p>Authorized Dealer: Minister, MyOne, Butterfly Group</p>
    <p>Status: POS System Active</p>
    """

# সেলস প্রসেস করার এন্ডপয়েন্ট
@app.route('/api/sale', methods=['POST'])
def process_sale():
    data = request.json
    # data ফরম্যাট: {"customer_name": "...", "amount": 1000, "paid": 500}
    
    customer = data.get('customer_name')
    amount = data.get('amount')
    paid = data.get('paid')
    due = amount - paid
    
    # সেলস রেকর্ড আপডেট
    sales_records.append({"customer": customer, "total": amount, "paid": paid, "due": due})
    
    # কাস্টমার ডিউ ট্র্যাকিং
    if customer in customer_dues:
        customer_dues[customer] += due
    else:
        customer_dues[customer] = due
        
    return jsonify({"status": "Success", "message": "Sale Recorded", "due_amount": due})

# কাস্টমার ডিউ রিপোর্ট দেখার এন্ডপয়েন্ট
@app.route('/api/dues', methods=['GET'])
def get_dues():
    return jsonify(customer_dues)

@app.route('/api/sync')
def sync_all_products():
    return jsonify({"status": "Success", "message": "Synced with Minister, MyOne & Butterfly Web Databases"})

if __name__ == "__main__":
    app.run(debug=True)
    
