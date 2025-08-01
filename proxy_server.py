from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/price')
def get_price_data():
    symbol = request.args.get('symbol')
    if not symbol:
        return jsonify({'error': 'symbol parameter is required'}), 400
    interval = request.args.get('interval', '15m')
    limit = request.args.get('limit', '100')

    url = f'https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}'
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Error fetching data: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
