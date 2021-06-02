from fbprophet import Prophet
from pytrends.request import TrendReq

def get_data(keyword):
    keyword = [keyword]
    pytrend = TrendReq()
    pytrend.build_payload(kw_list=keyword)
    df = pytrend.interest_over_time()
    df.drop(columns=['isPartial'], inplace=True)
    df.reset_index(inplace=True)
    df.columns = ["ds", "y"]
    return df


# make forecasts for a new period
def make_pred(df, periods):
    prophet_basic = Prophet()
    prophet_basic.fit(df)
    future = prophet_basic.make_future_dataframe(periods=periods)
    forecast = prophet_basic.predict(future)
    fig1 = prophet_basic.plot(forecast, xlabel="date", ylabel="trend", figsize=(10, 6))
    fig2 = prophet_basic.plot_components(forecast)
    forecast = forecast[["ds", "yhat"]]
    return forecast, fig1, fig2
def g_trend():
    pytrends = TrendReq(hl = 'en-US', tz = 360)
    hd = pytrends.trending_searches(pn = 'united_states')
    with open ('txtfile/g_trend','w') as file:
        for tag in hd:
            file.write(tag)


keyword = 'Gold'
periods=90
df = get_data(keyword)
forecast, fig1, fig2 = make_pred(df, periods)

fig1.savefig('output/trend1.png')
fig2.savefig('output/trend2.png')

