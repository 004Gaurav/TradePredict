import sys
import logging
import pandas as pd
import yfinance as yf

from Trade_prediction_system.exception import CustomException
from Trade_prediction_system.logger import logger

def fetch_stock_data(ticker: str, start_date: str, end_date: str) -> pd.DataFrame:
    """
    Fetch stock data using yfinance.
    """
    logger.info(f"Fetching stock data for {ticker} from {start_date} to {end_date}")
    
    try:
        df = yf.download(ticker, start=start_date, end=end_date)
        if df.empty:
            raise ValueError(f"No data found for ticker: {ticker}")
        
        logger.info(f"Successfully fetched data with shape: {df.shape}")
        return df
    
    except Exception as ex:
        logger.error(f"Error fetching data for {ticker}: {ex}")
        raise CustomException(ex, sys)
