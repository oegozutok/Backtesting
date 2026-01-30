import yfinance as yf
import vectorbt as vbt
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# 1. DATA
symbols = ["CL=F", "ZC=F", "ZS=F"]
raw = yf.download(
    symbols,
    start="2023-01-01",
    end="2026-01-29",
    auto_adjust=True
)
data = raw["Close"].dropna()
data.columns = data.columns.astype(str)
print(f"Data shape: {data.shape}")
print(f"Data columns: {data.columns.tolist()}")
# 2. INDICATORS
bbands = vbt.BBANDS.run(data)
rsi = vbt.RSI.run(data)
# 3. Align column names
bb_lower = pd.DataFrame(bbands.lower.values, index=data.index, columns=data.columns)
bb_upper = pd.DataFrame(bbands.upper.values, index=data.index, columns=data.columns)
rsi_val = pd.DataFrame(rsi.rsi.values, index=data.index, columns=data.columns)
# 4. SIGNALS
entries = (data < bb_lower) & (rsi_val < 30)
exits = (data > bb_upper) | (rsi_val > 70)
# 5. BACKTEST
pf = vbt.Portfolio.from_signals(
    data,
    entries,
    exits,
    init_cash=100_000,
    fees=0.0015,
    slippage=0.001,
    freq="D"
)
# 6. RESULTS
print("\n--- STRATEGY PERFORMANCE ---")
print(pf.stats())
# Plot each symbol separately (Plotly figures)
for col in data.columns:
    fig = pf[col].plot()
    fig.update_layout(title=f"Portfolio: {col}")
    fig.show()
# Correlation heatmap (matplotlib)
plt.figure(figsize=(10, 6))
sns.heatmap(data.pct_change().corr(), annot=True, cmap="RdYlGn", center=0)
plt.title("Commodity Returns Correlation Matrix")
plt.tight_layout()
plt.show()
# Individual returns per symbol
print("\n--- RETURNS BY SYMBOL ---")
for col in data.columns:
    ret = pf[col].total_return() * 100
    print(f"{col}: {ret:.2f}%")
print(f"\nAverage Portfolio Return: {pf.total_return().mean() * 100:.2f}%")
