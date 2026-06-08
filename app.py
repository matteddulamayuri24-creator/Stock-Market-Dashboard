import streamlit as st
from stock_analysis import get_stock_data
from charts import create_chart

st.title("📈 Stock Market Dashboard")
st.sidebar.header("Settings")

period = st.sidebar.selectbox(
    "Select Period",
    ["1mo", "3mo", "6mo", "1y", "5y"]
)

symbol = st.text_input("Enter Stock Symbol", "AAPL")

if symbol:
    data = get_stock_data(symbol, period)

    st.subheader(f"{symbol} Stock Data")
    st.dataframe(data.tail())

    # Step 7: Moving Average
    data["MA50"] = data["Close"].rolling(50).mean()
    st.line_chart(data[["Close", "MA50"]])

    # Step 8: Statistics
    st.write("Highest Price:", round(data["High"].max(), 2))
    st.write("Lowest Price:", round(data["Low"].min(), 2))
    st.write("Average Close:", round(data["Close"].mean(), 2))

    # Step 9: Download CSV
    csv = data.to_csv().encode('utf-8')

    st.download_button(
        "Download Data",
        csv,
        "stock_data.csv",
        "text/csv"
    )

    # Existing chart
    chart = create_chart(data)
    st.plotly_chart(chart)