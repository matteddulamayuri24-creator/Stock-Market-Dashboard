import plotly.graph_objects as go

def create_chart(data):
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=data.index,
            y=data["Close"],
            mode="lines",
            name="Close Price",
            line=dict(width=2)
        )
    )

    fig.update_layout(
        title="Interactive Stock Price Chart",
        xaxis_title="Date",
        yaxis_title="Price (USD)",
        hovermode="x unified",
        template="plotly_white"
    )

    return fig