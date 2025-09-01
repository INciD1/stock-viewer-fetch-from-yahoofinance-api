import yfinance as yf
import json
import sys
import pandas as pd
import pandas_ta as ta

def calculate_rsi(data):
    df = pd.DataFrame({"Close": data["c"]})
    rsi = ta.rsi(df["Close"], length=14)
    return rsi.iloc[-1] if len(rsi) >= 14 else None

def calculate_ma50(data):
    df = pd.DataFrame({"Close": data["c"]})
    ma50 = ta.sma(df["Close"], length=50)
    return ma50.iloc[-1] if len(ma50) >= 50 else None

def calculate_support_resistance(data):
    closes = pd.Series(data["c"])
    if len(closes) < 10:
        return None, None
    support = closes.tail(10).min()
    resistance = closes.tail(10).max()
    return support, resistance

def get_recommendation(current_price, target_price, rsi, ma50):
    if not target_price and (rsi is None or ma50 is None):
        return "hold", "ไม่มีข้อมูลเพียงพอ"

    # Strong Buy: ราคาต่ำกว่าราคาเป้าหมายมาก และ RSI ต่ำ
    if target_price and current_price < target_price * 0.90 and rsi and rsi < 30:
        return "strong buy", "ราคาต่ำกว่าราคาเป้าหมายมากและ RSI ต่ำ"
    # Buy: ราคาต่ำกว่าราคาเป้าหมาย หรือ RSI ต่ำ
    elif (target_price and current_price < target_price * 0.95) or (rsi and rsi < 40):
        return "buy", "ราคาเหมาะสมหรือ RSI ต่ำ"
    # Hold: ราคาใกล้ MA50 หรือ RSI ปกติ
    elif ma50 and abs(current_price - ma50) / ma50 < 0.05 and rsi and 40 <= rsi <= 60:
        return "hold", "ราคาใกล้เส้นค่าเฉลี่ย"
    # Sell: ราคาสูงกว่าราคาเป้าหมาย หรือ RSI สูง
    elif (target_price and current_price > target_price * 1.05) or (rsi and rsi > 70):
        return "sell", "ราคาสูงหรือ RSI สูง"
    # Strong Sell: ราคาสูงกว่าราคาเป้าหมายมากและ RSI สูง
    elif target_price and current_price > target_price * 1.10 and rsi and rsi > 80:
        return "strong sell", "ราคาสูงกว่าราคาเป้าหมายมากและ RSI สูง"
    else:
        return "hold", "สถานการณ์ปกติ"

def fetch_stock_data(symbol):
    try:
        ticker = yf.Ticker(symbol)
        hist = ticker.history(period="3mo", interval="1d")
        if hist.empty:
            return {"error": f"No data available for {symbol}"}

        data = {
            "s": "ok",
            "c": hist["Close"].tolist(),
            "h": hist["High"].tolist(),
            "l": hist["Low"].tolist(),
            "o": hist["Open"].tolist(),
            "v": hist["Volume"].tolist(),
            "t": (hist.index.astype('int64') // 10**9).tolist()
        }

        # Additional Data
        info = ticker.info
        data["name"] = info.get("longName", "Unknown")
        data["marketCap"] = info.get("marketCap", None)
        data["peRatio"] = info.get("trailingPE", None)

        # Technical Analysis
        data["rsi"] = calculate_rsi(data)
        data["ma50"] = calculate_ma50(data)
        support, resistance = calculate_support_resistance(data)
        data["support"] = support
        data["resistance"] = resistance

        # Recommendations
        current_price = data["c"][-1]
        target_price = info.get("targetMeanPrice", None)
        recommendation, recommendation_text = get_recommendation(current_price, target_price, data["rsi"], data["ma50"])
        data["recommendations"] = {"recommendation": recommendation}
        data["targetPrice"] = target_price
        data["recommendationText"] = recommendation_text

        # Technical Text
        data["technicalText"] = "วิเคราะห์จาก RSI, MA50, แนวรับ/แนวต้าน" if data["rsi"] and data["ma50"] else "ข้อมูลไม่เพียงพอ"

        return data
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"error": "No symbol provided"}))
        sys.exit(1)
    symbol = sys.argv[1]
    result = fetch_stock_data(symbol)
    print(json.dumps(result))