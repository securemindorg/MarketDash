# Market Dashboard

A clean, modern dashboard for tracking cryptocurrency, stocks, and market news in real-time.

![Dashboard Screenshot](screenshot.png)

## Features

- 📊 Real-time market data visualization
  - Bitcoin (BTC) 24-hour price chart
  - CISCO (CSCO) weekly stock performance
  - S&P 500 (FXAIX) weekly fund tracking
  - (or whatever you want to set them to)
- 📰 Live cryptocurrency news feed
- 🌙 Dark theme with clean interface
- 📱 Responsive design
- 📈 Interactive charts with time and price tooltips

## Prerequisites

- Python 3.x
- pip (Python package manager)
- CryptoCompare API key (free)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/market-dashboard.git
cd market-dashboard
```

2. Install required packages:
```bash
pip install flask yfinance requests pytz
```

3. Set up your CryptoCompare API key:
```bash
export CRYPTOCOMPARE_API_KEY='your_api_key_here'
```

Get your free API key from [CryptoCompare](https://min-api.cryptocompare.com/)

## Usage

1. Start the Flask server:
```bash
python app.py
```

2. Visit `http://localhost:5000` in your web browser

The dashboard will display:
- Left panel: Latest cryptocurrency news
- Right panel (top): Bitcoin price chart (24h)
- Right panel (middle): CISCO stock price (weekly)
- Right panel (bottom): S&P 500 fund price (weekly)

## Data Sources

- Cryptocurrency data: Yahoo Finance (BTC-USD)
- Stock data: Yahoo Finance (CSCO)
- Index fund data: Yahoo Finance (FXAIX)
- News feed: CryptoCompare API

## Customization

### Modifying Chart Timeframes

In `app.py`, adjust the time intervals in the `get_market_data` function:

```python
if symbol == 'BTC':
    # Modify Bitcoin timeframe
    start_time = end_time - timedelta(days=1)
    interval = '1h'
else:
    # Modify stock timeframe
    start_time = end_time - timedelta(days=7)
    interval = '1d'
```

### Styling

Customize the appearance by modifying `static/css/style.css`:
- Background opacity: `.market-widget { background: rgba(0, 0, 0, 0.7); }`
- Accent color: `.widget-title { color: #228B22; }`
- Layout spacing: `.market-container { gap: 20px; }`

## Browser Support

- Chrome (recommended)
- Firefox
- Safari
- Edge

## Troubleshooting

1. **No market data displaying**
   - Check internet connection
   - Verify Yahoo Finance API access
   - Ensure correct symbol mapping in `app.py`

2. **News feed not loading**
   - Verify CRYPTOCOMPARE_API_KEY is set
   - Check API rate limits
   - Ensure internet connectivity

3. **Charts not rendering**
   - Check browser console for errors
   - Verify TradingView library is loading
   - Clear browser cache

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
