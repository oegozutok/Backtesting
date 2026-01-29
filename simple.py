import vectorbt as vbt
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# 1. SETTINGS & ASSET SELECTION
# CL=F: Crude Oil (Energy) | ZC=F: Corn (Agri) | ZS=F: Soybeans (Agri)
symbols = ["CL=F", "ZC=F", "ZS=F"]
start_date = "2023-01-01"
end_date = "2026-01-29"

print(f"--- Initializing Backtest for {symbols} ---")

# 2. DATA INGESTION (ETL)
# Pulling Daily OHLCV data
data = yf.download(symbols, start=start_date, end=end_date)['Close']

# 3. STRATEGY: DUAL MOVING AVERAGE CROSSOVER
# Fast MA (Short-term momentum) vs Slow MA (Long-term trend)
fast_ma = vbt.MA.run(data, 10)
slow_ma = vbt.MA.run(data, 50)

# Signal Logic: 
# Long (Entry) when 10-day crosses ABOVE 50-day
# Short (Exit) when 10-day crosses BELOW 50-day
entries = fast_ma.ma_crossed_above(slow_ma)
exits = fast_ma.ma_crossed_below(slow_ma)

# 4. SIMULATION ENGINE
# init_cash: $100k | freq: Daily | fees: 0.1% (Commisison simulation)
pf = vbt.Portfolio.from_signals(
    data, 
    entries, 
    exits, 
    init_cash=100000, 
    fees=0.001, 
    freq='D'
)

# 5. QUANT METRICS OUTPUT
# This is what you show the hiring manager
print("\n--- PERFORMANCE METRICS ---")
stats = pf.stats()
print(stats)

# 6. VISUALIZATION
# Plotting cumulative returns to show the strategy "Alpha"
pf.plot().show()
