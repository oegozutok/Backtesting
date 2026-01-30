import yfinance as yf
import vectorbt as vbt
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 1. DATA ACQUISITION: Energy, Agriculture, and the USD Index (Macro Factor)
symbols = ["CL=F", "ZC=F", "ZS=F", "DX-Y.NYB"] 
data = yf.download(symbols, start="2023-01-01", end="2026-01-29")['Close']

# 2. FEATURE ENGINEERING: Technical Indicators
# Bollinger Bands (20-day, 2 Std Dev)
bbands = vbt.BBANDS.run(data, window=20, alpha=2)
# RSI (14-day)
rsi = vbt.RSI.run(data, window=14)
# ATR for Volatility (14-day)
atr = vbt.ATR.run(data['CL=F'], data['CL=F'], data['CL=F'], window=14) # Example for Oil

# 3. STRATEGY LOGIC: Mean Reversion
# LONG: Price crosses BELOW Lower Band AND RSI is Oversold (<30)
entries = (data < bbands.lower) & (rsi.rsi < 30)
# EXIT: Price crosses ABOVE Upper Band OR RSI is Overbought (>70)
exits = (data > bbands.upper) | (rsi.rsi > 70)

# 4. SIMULATION: Vectorized Portfolio
# Adding 0.15% slippage/commissions to be realistic for Commodities
pf = vbt.Portfolio.from_signals(
    data, entries, exits, 
    init_cash=100000, 
    fees=0.0015, 
    slippage=0.001,
    freq='D'
)

# 5. ADVANCED ANALYSES
print("--- STRATEGY PERFORMANCE ---")
print(pf.stats())

# 6. VISUALIZATIONS
# A. Equity Curve (Cumulative Returns)
pf.plot().show()

# B. Correlation Matrix: How do these commodities move together?
plt.figure(figsize=(10,6))
sns.heatmap(data.pct_change().corr(), annot=True, cmap='coolwarm')
plt.title("Commodity Returns Correlation Matrix")
plt.show()

# C. Drawdown Analysis (Underwater Plot)
pf.drawdowns.plot().show()
