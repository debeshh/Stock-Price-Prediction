from flask import Flask, request, jsonify
import yfinance as yf
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import Ridge

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    symbol = data['symbol'].upper()
    
    # Download latest stock data (last 5 days)
    stock = yf.download(symbol, period="5d")
    if stock.empty:
        return jsonify({'error': 'Invalid stock symbol'}), 400

    stock.dropna(inplace=True)

    # Prepare features
    X = stock[['Open', 'High', 'Low', 'Volume']].values
    y = stock['Close'].values

    # Train model on available data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    poly = PolynomialFeatures(degree=2, include_bias=False)
    X_poly = poly.fit_transform(X_scaled)

    model = Ridge(alpha=1.0)
    model.fit(X_poly, y)

    # Predict the next day's closing price (based on the latest row)
    latest = stock.iloc[-1][['Open', 'High', 'Low', 'Volume']].values.reshape(1, -1)
    latest_scaled = scaler.transform(latest)
    latest_poly = poly.transform(latest_scaled)
    predicted_price = model.predict(latest_poly)[0]

    return jsonify({
        'stock': symbol,
        'predicted_price': round(predicted_price, 2)
    })

if __name__ == '__main__':
    app.run(debug=True)