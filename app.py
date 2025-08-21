import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np

st.title("📈 AI株価予測（デモ）")

# 対象銘柄（例: トヨタ・ソニー・ルネサス）
symbols = {"トヨタ": "7203.T", "ソニー": "6758.T", "ルネサス": "6723.T"}

data = {}
for name, code in symbols.items():
    df = yf.download(code, period="3mo", interval="1d")
    df["Return"] = df["Close"].pct_change()
    data[name] = df

# 予測スコア（ここでは単純に過去5日間の平均リターン）
scores = {name: df["Return"].tail(5).mean() for name, df in data.items()}
ranking = sorted(scores.items(), key=lambda x: x[1], reverse=True)

st.subheader("予測ランキング")
for rank, (name, score) in enumerate(ranking, 1):
    st.write(f"{rank}位 {name} : {score:.2%}")
