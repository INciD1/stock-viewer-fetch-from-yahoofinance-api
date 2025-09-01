# 📈 Stock & ETF Analyzer

## Overview
**Stock & ETF Analyzer** is a web application that analyzes U.S. stocks and ETFs (NASDAQ & NYSE) using data from the **Yahoo Finance API**.  
It provides real-time quotes, technical indicators, and simple recommendations to help users explore market trends.  

⚠️ **Disclaimer:**  
- This project is for **educational purposes only**.  
- **This is not financial or investment advice.**  
- Always do your own research and consult a licensed advisor before investing.  

---

## Features
- 🔍 Search stocks and ETFs by symbol (e.g., `AAPL`, `GOOGL`, `TSLA`, `SPY`)  
- 📊 Real-time stock & ETF data from Yahoo Finance  
- 📈 Technical indicators:  
  - EMA (Exponential Moving Average)  
  - RSI (Relative Strength Index)  
  - Support & Resistance levels  
- 🟢🔴 Buy/Hold/Sell recommendations  
- 📉 Target price and stop loss levels  
- ⚡ Backend caching for faster responses  
- 🐍 Python helper script for advanced stock analysis  

---

## Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/stock-etf-analyzer.git
cd stock-etf-analyzer
```

---

### 2. Backend (Node.js + Express)

#### Install dependencies
```bash
npm install
```

#### Run backend server
```bash
npm start
```

For development (with auto-reload using nodemon):
```bash
npm run dev
```

By default, the server will start at:
```
http://localhost:3000
```

---

### 3. Python Script (fetch_stock.py)

This project includes a Python helper script to fetch and analyze stock data directly.  

#### Install dependencies
```bash
pip install yfinance pandas pandas_ta
```

#### Run the script
```bash
python fetch_stock.py AAPL
```

#### Example output (JSON)
```json
{
  "s": "ok",
  "name": "Apple Inc.",
  "marketCap": 2750000000000,
  "rsi": 45.7,
  "ma50": 172.34,
  "support": 165.2,
  "resistance": 179.8,
  "recommendations": {
    "recommendation": "hold"
  },
  "targetPrice": 190.0,
  "recommendationText": "near 50-day moving average"
}
```

---

## Example Usage

### Node.js Backend (API request)
```bash
curl http://localhost:3000/api/stock/AAPL
```

Example response:
```json
{
  "symbol": "AAPL",
  "price": 174.36,
  "change": -0.52,
  "rsi": 48.2,
  "ema20": 176.4,
  "support": 170.0,
  "resistance": 180.5,
  "recommendation": "hold"
}
```

---

## Tech Stack
- **Backend**: Node.js, Express.js  
- **Python Script**: yfinance, pandas, pandas_ta  
- **Frontend (Optional)**: HTML, CSS, JavaScript, Chart.js  
- **API**: Yahoo Finance  

---

## Limitations
- Data may not always be real-time due to API restrictions.  
- API rate limits may cause incomplete data.  
- CORS policy may require running via backend server.  

---

## ⚠️ Disclaimer
This project is for **educational purposes only**.  
It is **not financial or investment advice**.  
Use this tool at your own risk.  

---
✨ *Learn responsibly. Invest wisely.* ✨
