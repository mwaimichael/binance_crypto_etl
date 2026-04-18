# Crypto & Assets Price ETL Pipeline
A simple ETL pipeline that sources the daily 24-hour average price of the select top cryptocurrencies and other assets from the Binance API, transforms the raw data into a structured format, and loads it into a PostgreSQL database — complete with a collection date timestamp.
Prices sourced are of the following crtpos/assets:
1. BTCUSDT
2. WBTCUSDT
3. USDTIDR
4. USDTBIDR
5. USDTIDRT
6. XAUTUSDT
7. PAXGUSDT
8. USDTCOP
9. YFIUSDT
10. WBETHUSDT

### Pipeline Architecture
Extract Transform Load

1. Extract - Queries the Binance REST API (GET /api/v3/ticker/24hr) to fetch 24-hour price statistics for each configured asset symbol.
2. Transform — Parses the raw JSON response and structures the data into a Pandas DataFrame with a collection date column.
3. Load — Appends the transformed records sequentially into a PostgreSQL database table.
