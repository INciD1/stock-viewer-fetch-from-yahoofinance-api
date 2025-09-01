# 📈 Stock & ETF Analyzer

## Overview
**Stock & ETF Analyzer** is a web-based application for analyzing U.S. stocks and ETFs (NASDAQ and NYSE).  
It provides real-time data, technical analysis, and simple recommendations to help users explore market trends.  

⚠️ **Disclaimer:** This project is for **educational purposes only** and **not financial or investment advice**.  

---

## How to Use

### 1. Search for Stocks
**Method 1: Manual Input**
1. Enter the **stock symbol** (e.g., `AAPL`, `GOOGL`, `TSLA`) in the search box.  
2. Select the stock market (All/NASDAQ/NYSE/AMEX/OTC) – *optional*.  
3. Click **"🔍 Analyze"** or press Enter.  

**Method 2: Quick Click Popular Stocks**
- Select from popular chips at the bottom:  
  - **Tech Stocks:** AAPL, GOOGL, MSFT, TSLA, NVDA  
  - **ETFs:** SPY, QQQ, VOO, VTI  

---

### 2. Reading Results

#### Basic Info
- **Company name & symbol**  
- **Current price** (green = up, red = down)  
- **Change** (absolute and %)  
- **Market Cap**  
- **Volume**  
- **Daily Range & 52-week range**  

#### Technical Analysis
- **EMA 20/50**: Exponential Moving Averages  
- **RSI**: Relative Strength Index (30 = oversold, 70 = overbought)  
- **Support & Resistance levels**  

#### Recommendations
System provides 5 levels:  
- 🟢 **Strong Buy**  
- 🟢 **Buy**  
- 🟡 **Hold**  
- 🔴 **Sell**  
- 🔴 **Strong Sell**  

#### Target Price
- **Target Price**: expected upside level  
- **Stop Loss**: suggested downside cutoff  

---

### 3. Price Chart
Charts show:  
- **Price line** (blue)  
- **EMA 20** (green dashed line)  
- **Support line** (red dashed line)  
- **Resistance line** (orange dashed line)  

---

## Recommended Stocks & ETFs

### 📊 Popular Stocks
| Symbol | Company | Category |
|--------|---------|----------|
| AAPL   | Apple Inc. | Technology |
| GOOGL  | Alphabet Inc. | Technology |
| MSFT   | Microsoft Corp. | Technology |
| TSLA   | Tesla Inc. | EV/Automotive |
| AMZN   | Amazon.com Inc. | E-Commerce |
| NVDA   | NVIDIA Corp. | Semiconductors |
| META   | Meta Platforms | Social Media |

### 📈 Popular ETFs
| Symbol | ETF Name | Description |
|--------|----------|-------------|
| SPY    | SPDR S&P 500 ETF | S&P 500 |
| QQQ    | Invesco QQQ Trust | NASDAQ 100 |
| VOO    | Vanguard S&P 500 ETF | Low-cost S&P 500 |
| VTI    | Vanguard Total Stock Market | Entire U.S. market |

---

## Buy & Sell Signals

### Buy Signals
- Price above EMA 20/50  
- RSI < 30 (oversold)  
- Price near support  
- Uptrend confirmation  

### Sell Signals
- Price below EMA  
- RSI > 70 (overbought)  
- Price near resistance  
- Downtrend confirmation  

---

## Limitations
- **CORS Policy**: May cause issues in some browsers.  
- **API Limitations**: Some data may be incomplete.  
- **Data Latency**: Not guaranteed to be real-time.  

---

## Tech Stack
- **Frontend**: HTML5, CSS3, JavaScript (ES6)  
- **Charts**: Chart.js  
- **API**: Yahoo Finance API  
- **Requests**: Axios  

---

## Troubleshooting

### Data not loading
1. Check internet connection.  
2. Try another browser.  
3. Verify the symbol.  
4. Refresh and retry.  

### Chart not displaying
1. Wait until data fully loads.  
2. Check browser console (F12).  
3. Try another stock.  

---

## ⚠️ Disclaimer
- This project is for **educational purposes only**.  
- **This is not financial or investment advice.**  
- Always do your own research and consult with a financial advisor before making investment decisions.  
- Investing in the stock market involves risks.  

---
✨ *Learn responsibly. Invest wisely.* ✨
