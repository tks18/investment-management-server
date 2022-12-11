from datetime import datetime
import yfinance as yf
from pandas import DataFrame, concat as concat_dfs, Timedelta
from app.plugins.dates import convert_date_to_string
from app.plugins.backend import api_methods
from app.plugins.environment import get_env_variable


def assign_date_id(row, token):
    date_id = api_methods["calendar"]["dateid"](token, row.name)
    return date_id


def download_ticker_data(ticker: str, start: datetime, end: datetime):
    ticker_interval = get_env_variable("TICKER_DATA_INTERVAL")
    return yf.download(
        ticker,
        start=start,
        end=end,
        interval=ticker_interval,
    )


def get_ticker_data(
    investment_master: DataFrame, start_date: datetime, end_date: datetime, token: str
) -> DataFrame:
    ticker_dfs = []
    for _, row in investment_master.iterrows():
        ticker_df = download_ticker_data(
            ticker=row["yahoo_ticker"],
            start=start_date,
            end=end_date,
        )
        if len(ticker_df) > 0:
            ticker_df.index = ticker_df.index + Timedelta(days=-1)
            ticker_df.columns = ticker_df.columns.str.lower()
            ticker_df = ticker_df.rename(columns={"adj close": "adj_close"})
            ticker_df["date"] = ticker_df.apply(
                lambda row: convert_date_to_string(row.name, "%Y-%m-%d"), axis=1
            )
            ticker_df["master_id"] = row["_id"]
            ticker_df["date_id"] = ticker_df.apply(
                lambda row: assign_date_id(row, token), axis=1
            )
            ticker_dfs.append(ticker_df)

    if len(ticker_dfs) > 0:
        all_ticker_df = concat_dfs(ticker_dfs)
        return all_ticker_df
    else:
        return []
