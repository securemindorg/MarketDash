from flask import Flask, render_template, jsonify
import yfinance as yf
from datetime import datetime, timedelta
import pytz
import requests
import os

app = Flask(__name__)

@app.route('/')
@app.route('/markets')
def markets():
    return render_template('markets.html')

@app.route('/api/market-data/<symbol>')
def get_market_data(symbol):
    try:
        # Map frontend symbols to Yahoo Finance symbols
        symbol_map = {
            'BTC': 'BTC-USD',
            'CISCO': 'CSCO',
            'SP500': 'FXAIX'
        }
        
        yf_symbol = symbol_map.get(symbol)
        if not yf_symbol:
            return jsonify({'error': f'Invalid symbol: {symbol}'}), 400

        ticker = yf.Ticker(yf_symbol)
        now = datetime.now(pytz.UTC)

        # Different date ranges for different symbols
        if symbol == 'BTC':
            # Bitcoin: last 24 hours
            end_time = now
            start_time = end_time - timedelta(days=1)
            interval = '1h'
        else:
            # Both CISCO and FXAIX: last week
            end_time = now
            start_time = end_time - timedelta(days=7)
            interval = '1d'

        # Fetch historical data
        df = ticker.history(start=start_time, end=end_time, interval=interval)
        
        if df.empty:
            return jsonify({'error': f'No data available for {symbol}'}), 404

        # Format data for the chart
        data = []
        for index, row in df.iterrows():
            data.append({
                'time': int(index.timestamp()),
                'value': float(row['Close'])
            })

        current_price = float(df['Close'].iloc[-1])
        high_price = float(df['High'].max())
        low_price = float(df['Low'].min())

        return jsonify({
            'data': data,
            'high': high_price,
            'low': low_price,
            'current': current_price,
            'last_update': int(df.index[-1].timestamp())
        })

    except Exception as e:
        print(f"Error processing {symbol}: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/crypto-news')
def get_crypto_news():
    try:
        api_key = os.getenv('CRYPTOCOMPARE_API_KEY', '')
        url = f'https://min-api.cryptocompare.com/data/v2/news/?lang=EN&api_key={api_key}'
        
        response = requests.get(url)
        if response.status_code == 200:
            news_data = response.json()
            # Limit to 9 news items
            formatted_news = []
            for item in news_data['Data'][:9]:
                formatted_news.append({
                    'title': item['title'],
                    'url': item['url'],
                    'source': item['source'],
                    'timestamp': item['published_on']
                })
            return jsonify(formatted_news)
        else:
            return jsonify({'error': 'Failed to fetch news'}), 500

    except Exception as e:
        print(f"Error fetching news: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 