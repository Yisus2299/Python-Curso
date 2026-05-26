import json
import os
import requests


# NOTA IMPORTANTE - El codigo funciona al 100% pero, Alpha Vantage tiene limites muy absurdos y venezuela esta bloqueada asi que se tuvo que adaptar el codigo para eso
# asi que, a esperar para probar este codigo. Se pudo completar gracias a la documentacion y investigar
# datos de la primera Api
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "8F7350UC5TV86YFK"
STOCK_NAME = "TSLA"

# datos de la segunda Api
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
    # Alpha Vantage suele responder con "Note" o "Information" cuando hay límite
    return isinstance(payload, dict) and ("Note" in payload or "Information" in payload)


    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

stock_json = load_cache(STOCK_CACHE_PATH)

if stock_json is None:
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK_NAME,
        "apikey": STOCK_API_KEY,
    }
    stock_json = alphavantage_get(params)

    if is_rate_limit(stock_json):
        # Si hoy ya te bloqueó, al menos te queda un mensaje claro
        print(stock_json)
        raise SystemExit

    save_cache(STOCK_CACHE_PATH, stock_json)

# Si la API responde con error/rate-limit, no existirá "Time Series (Daily)"
if "Time Series (Daily)" not in stock_json:
    print(stock_json)
    raise SystemExit
else:
    data = stock_json["Time Series (Daily)"]

    # Ordenar fechas para asegurar "ayer" y "antes de ayer"
    dates = sorted(data.keys(), reverse=True)
    yesterday = dates[0]
    day_before_yesterday = dates[1]

    yesterday_data = data[yesterday]
    yesterday_closing_price = yesterday_data["4. close"]
    print(yesterday_closing_price)

#TODO 2. - Get the day before yesterday's closing stock price
    day_before_yesterday_data = data[day_before_yesterday]
    day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
    print(day_before_yesterday_closing_price)

 #TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
    difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price)) #abs lo convierte a positivo
    print(difference)

 #TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
    # % cambio respecto al día anterior (lo más común)
    diff_percent = (difference / float(day_before_yesterday_closing_price)) * 100
    print(diff_percent)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
    if diff_percent > 5:
        print("Get News")

        ## STEP 2: https://newsapi.org/
        # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

        # NOTA: usamos Alpha Vantage NEWS_SENTIMENT para evitar NewsAPI (tu VPN es extensión del navegador).
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

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
        first_three = feed[:3]

        ## STEP 3: Use twilio.com/docs/sms/quickstart/python
        #to send a separate message with each article's title and description to your phone number.

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
        formatted_articles = [
            f"{STOCK_NAME}: {'🔺' if float(yesterday_closing_price) > float(day_before_yesterday_closing_price) else '🔻'}{abs(diff_percent):.2f}%\n"
            f"Headline: {a.get('title', 'N/A')}\n"
            f"Brief: {a.get('summary', 'N/A')}"
            for a in first_three
        ]

        for item in formatted_articles:
            print(item)
            print()

#TODO 9. - Send each article as a separate message via Twilio.


#Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""