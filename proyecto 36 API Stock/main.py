import json
import os
import requests


# IMPORTANT NOTE - The code is functionally complete but Alpha Vantage enforces strict rate limits
# and the service may be restricted from certain locations; you may need to adapt or cache
# requests for reliable testing.
# Stock API details
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "8F7350UC5TV86YFK"
STOCK_NAME = "TSLA"

# News / sentiment API details
COMPANY_NAME = "Tesla Inc"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "4152daf86f024426acf342a93c83657f"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STOCK_CACHE_PATH = os.path.join(BASE_DIR, f"stock_{STOCK_NAME}_daily.json")
NEWS_CACHE_PATH = os.path.join(BASE_DIR, f"news_{STOCK_NAME}.json")


def load_cache(path: str):
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_cache(path: str, payload):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)


def alphavantage_get(params: dict, timeout: int = 15):
    r = requests.get(STOCK_ENDPOINT, params=params, timeout=timeout)
    r.raise_for_status()
    return r.json()


def is_rate_limit(payload: dict) -> bool:
    # Alpha Vantage returns a "Note" or "Information" key when rate limited
    return isinstance(payload, dict) and ("Note" in payload or "Information" in payload)


## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# TODO 1. - Get yesterday's closing stock price.
stock_json = load_cache(STOCK_CACHE_PATH)

if stock_json is None:
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK_NAME,
        "apikey": STOCK_API_KEY,
    }
    stock_json = alphavantage_get(params)

    if is_rate_limit(stock_json):
        # If the response indicates rate limiting, print the message and exit
        print(stock_json)
        raise SystemExit

    save_cache(STOCK_CACHE_PATH, stock_json)

# If the API response is an error or rate-limit, it won't contain "Time Series (Daily)"
if "Time Series (Daily)" not in stock_json:
    print(stock_json)
    raise SystemExit
else:
    data = stock_json["Time Series (Daily)"]

    # Sort dates to ensure we pick "yesterday" and the day before
    dates = sorted(data.keys(), reverse=True)
    yesterday = dates[0]
    day_before_yesterday = dates[1]

    yesterday_data = data[yesterday]
    yesterday_closing_price = yesterday_data["4. close"]
    print(yesterday_closing_price)

    # TODO 2 - Get the day before yesterday's closing price
    day_before_yesterday_data = data[day_before_yesterday]
    day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
    print(day_before_yesterday_closing_price)

    # TODO 3 - Find the positive difference between the two closing prices
    difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))  # abs() makes it positive
    print(difference)

    # TODO 4 - Compute the percentage difference between yesterday and the day before
    diff_percent = (difference / float(day_before_yesterday_closing_price)) * 100
    print(diff_percent)

    # TODO 5 - If the percent change is greater than 5, fetch news
    if diff_percent > 5:
        print("Get News")

        # STEP 2: Use News / sentiment API
        # Instead of just printing "Get News", retrieve the first 3 news items for the COMPANY_NAME.

        # NOTE: we use Alpha Vantage NEWS_SENTIMENT in this example to avoid external NewsAPI constraints.
        news_json = load_cache(NEWS_CACHE_PATH)

        if news_json is None:
            news_params = {
                "function": "NEWS_SENTIMENT",
                "tickers": STOCK_NAME,
                "apikey": STOCK_API_KEY,
            }
            news_json = alphavantage_get(news_params)

            if is_rate_limit(news_json):
                print(news_json)
                raise SystemExit

            save_cache(NEWS_CACHE_PATH, news_json)

        if "feed" not in news_json:
            print(news_json)
            raise SystemExit

        feed = news_json["feed"]

        # TODO 7 - Take the first three articles using slicing
        first_three = feed[:3]

        # STEP 3: Prepare messages (e.g., for SMS via Twilio)

        # TODO 8 - Build a list of formatted strings for the first three articles
        formatted_articles = [
            f"{STOCK_NAME}: {'🔺' if float(yesterday_closing_price) > float(day_before_yesterday_closing_price) else '🔻'}{abs(diff_percent):.2f}%\n"
            f"Headline: {a.get('title', 'N/A')}\n"
            f"Brief: {a.get('summary', 'N/A')}"
            for a in first_three
        ]

        for item in formatted_articles:
            print(item)
            print()

        # TODO 9 - Send each article as a separate message via Twilio (not implemented here)


        # Optional message format example:
        # TSLA: 🔺2%
        # Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?
        # Brief: We at Insider Monkey have gone over 821 13F filings ...