import yfinance as yf

def fetch_financials(ticker: str):
    """
    Fetches financial statements (income, balance sheet, cash flow)
    for a given company ticker using Yahoo Finance.
    """
    stock = yf.Ticker(ticker)
    income_statement = stock.financials
    balance_sheet = stock.balance_sheet
    cash_flow = stock.cashflow
    return {
        "income_statement": income_statement,
        "balance_sheet": balance_sheet,
        "cash_flow": cash_flow
    }

if __name__ == "__main__":
    ticker = "AAPL" # Apple Inc.

    financials = fetch_financials(ticker)

    for key, df in financials.items():
        df.to_csv(f"data/{ticker}_{key}.csv")
        print(f"Saved {key} for {ticker}")