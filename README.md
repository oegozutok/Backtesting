# Commodity Alpha  
### Multi-Asset Mean Reversion Framework

## Executive Summary
**Commodity Alpha** is a high-performance quantitative backtesting framework designed to simulate **mean reversion strategies** across **Energy** (Crude Oil) and **Agricultural** (Corn, Soybeans) futures markets.

Built with **vectorized execution**, the framework evaluates volatility-adjusted entry logic while incorporating real-world trading frictions such as **slippage** and **transaction costs**.

This project was developed as a technical deep dive into commodity market dynamics during participation in the **CME Group Trading Challenge**.

---

## 🛠 Tech Stack

**Language**
- Python 3.10+

**Core Libraries**
- `vectorbt` — Vectorized backtesting engine  
- `pandas` — Time-series analysis  
- `yfinance` — Market data ingestion  

**Visualization**
- Plotly  
- Matplotlib  
- Seaborn  

**Mathematical Modeling**
- NumPy  
- SciPy  

---

## 📈 Strategic Methodology

The core strategy implements a **Bollinger Band Mean Reversion model** enhanced with a **momentum filter**.

Commodity futures often trade within **range-bound regimes** driven by seasonal supply-demand cycles, making them well-suited for mean-reverting logic when combined with volatility-aware risk controls.

---

## Mathematical Foundation

An entry signal is triggered when the asset price deviates significantly from its rolling mean:

\[
P_t < \mu - (k \cdot \sigma)
\]

Where:
- \(\mu\) = 20-day Simple Moving Average  
- \(\sigma\) = Rolling standard deviation  
- \(k\) = Threshold multiplier (set to 2.0, approximating a 95% confidence interval)

---

## Risk Management & Constraints

- **Volatility Scaling**  
  Position sizing is adjusted using **Average True Range (ATR)** to normalize risk across assets with differing volatility profiles.

- **Slippage Simulation**  
  - 0.1% slippage per trade  
  - 0.05% commission fee  
  These constraints ensure results reflect institutional-grade execution realities.

---

## 📊 Performance & Analytics

The framework produces a comprehensive suite of **quant-first performance metrics**:

| Metric | Definition |
|------|-----------|
| Sharpe Ratio | Risk-adjusted return relative to volatility |
| Max Drawdown | Peak-to-trough decline during the simulation |
| Profit Factor | Ratio of gross profits to gross losses |
| Win Rate | Percentage of profitable trade exits |

---

## 🚀 Installation & Usage

Clone the repository:
```bash
git clone https://github.com/oegozutok/commodity-alpha.git
````

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the simulation:

```bash
python main.py
```

---

## 🔍 Key Insights

* **Correlation Analysis**
  Energy and Agricultural futures often exhibit **low correlation**, enabling meaningful **portfolio diversification benefits**.

* **Regime Sensitivity**
  The strategy performs best in **low-volatility, sideways markets**, while experiencing drawdowns during **macro-driven trend breakouts**.

---

## About the Author

**Orhan Emir Gozutok**
B.S. in Statistics & Data Science, University of Arizona (GPA: 3.87)

Specialist in **applied stochastic processes**, **quantitative research**, and **production-level data engineering**.
