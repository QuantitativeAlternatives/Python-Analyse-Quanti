import yfinance as yf
import pandas as pd
import plotly.graph_objs as go

# Collecter les données de prix des indices
cac40 = yf.download("^FCHI", start="2018-01-01", end="2023-08-22")
sp500 = yf.download("^GSPC", start="2018-01-01", end="2023-08-22")
nasdaq = yf.download("^IXIC", start="2018-01-01", end="2023-08-22")

# Calculer la volatilité avec une fenêtre de 30 jours (peut être ajustée)
rolling_volatility_cac40 = cac40["Close"].pct_change().rolling(window=30).std()
rolling_volatility_sp500 = sp500["Close"].pct_change().rolling(window=30).std()
rolling_volatility_nasdaq = nasdaq["Close"].pct_change().rolling(window=30).std()

# Créer des traces pour chaque rolling volatility
trace_cac40 = go.Scatter(x=rolling_volatility_cac40.index, y=rolling_volatility_cac40, mode="lines", name="CAC 40")
trace_sp500 = go.Scatter(x=rolling_volatility_sp500.index, y=rolling_volatility_sp500, mode="lines", name="S&P 500")
trace_nasdaq = go.Scatter(x=rolling_volatility_nasdaq.index, y=rolling_volatility_nasdaq, mode="lines", name="Nasdaq")

# Créer la figure et ajouter les traces
fig = go.Figure(data=[trace_cac40, trace_sp500, trace_nasdaq])

# Mise en forme du graphique interactif
fig.update_layout(
    title="Rolling Volatility Comparison",
    xaxis_title="Date",
    yaxis_title="Rolling Volatility",
    xaxis_rangeslider_visible=True,  # Ajouter un slider pour zoomer
    showlegend=True  # Afficher la légende
)

# Afficher le graphique interactif dans le navigateur web
fig.show()
