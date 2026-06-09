from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Brewery Finder</title>
  <style>
    body { font-family: Arial, sans-serif; max-width: 900px; margin: 2rem auto; padding: 0 1rem; }
    h1 { color: #2c3e50; }
    form { margin-bottom: 1.5rem; }
    input[type=text] { width: 250px; padding: 0.4rem; }
    button { padding: 0.5rem 0.8rem; }
    .brewery { border: 1px solid #ddd; border-radius: 8px; padding: 1rem; margin-bottom: 1rem; }
    .brewery h2 { margin: 0 0 0.3rem; }
    .meta { color: #555; }
  </style>
</head>
<body>
  <h1>Brewery Finder</h1>
  <p>Search breweries by city using the Open Brewery DB public API.</p>
  <form method="get">
    <label>
      City:
      <input type="text" name="city" value="{{ city or '' }}" placeholder="e.g. denver">
    </label>
    <button type="submit">Search</button>
  </form>

  {% if error %}
    <p style="color: red;">{{ error }}</p>
  {% endif %}

  {% if breweries %}
    <p>Found {{ breweries|length }} breweries in <strong>{{ city }}</strong>:</p>
    {% for b in breweries %}
      <div class="brewery">
        <h2>{{ b.name }}</h2>
        <div class="meta">{{ b.brewery_type | capitalize }} brewery</div>
        <p>
          {{ b.street or 'Address not available' }}<br>
          {{ b.city }}, {{ b.state }} {{ b.postal_code }}
        </p>
        {% if b.website_url %}
          <p><a href="{{ b.website_url }}" target="_blank">Visit website</a></p>
        {% endif %}
      </div>
    {% endfor %}
  {% elif city %}
    <p>No breweries found for "{{ city }}". Try another city.</p>
  {% endif %}
</body>
</html>
"""

@app.route("/")
def index():
    city = request.args.get("city", "").strip()
    breweries = []
    error = None

    if city:
        try:
            url = "https://api.openbrewerydb.org/v1/breweries"
            params = {"by_city": city, "per_page": 25}
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            breweries = response.json()
        except requests.RequestException as exc:
            error = f"Could not fetch breweries: {exc}"

    return render_template_string(TEMPLATE, city=city, breweries=breweries, error=error)

if __name__ == "__main__":
    app.run(debug=True)