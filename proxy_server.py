from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Crypto Proxy API is live 🔥"})

@app.route('/price-data')
def get_price_data():
    symbol = request.args.get('symbol')
    interval = request.args.get('interval', '15m')
    limit = request.args.get('limit', '100')

    if not symbol:
        return jsonify({"error": "Symbol parameter is required"}), 400

    url = f'https://api.binance.com/api/v3/klines?symbol={symbol}USDT&interval={interval}&limit={limit}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
