import csv
import requests
from pathlib import Path
from bs4 import BeautifulSoup

BASE_DIR = Path(__file__).resolve().parent
csv_path = BASE_DIR / "nutrition.csv"

url = "https://www.nutritionvalue.org/Pasta%2C_enriched%2C_dry_nutritional_value.html"

response = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"},
    timeout=15,
)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

def normalize(text: str) -> str:
    return " ".join(text.lower().split())

rows = []

for table in soup.find_all("table"):
    table_rows = []
    for tr in table.find_all("tr"):
        cells = [cell.get_text(separator=" ", strip=True) for cell in tr.find_all(["th", "td"])]
        if cells:
            table_rows.append(cells)

    if not table_rows:
        continue

    header_index = None
    for index, row in enumerate(table_rows):
        row_texts = [normalize(cell) for cell in row]
        joined = " ".join(row_texts)
        if "nutrient" in joined and "amount" in joined and "dv" in joined:
            header_index = index
            break

    if header_index is None:
        continue

    for row in table_rows[header_index + 1:]:
        if len(row) < 2:
            continue

        nutrient = row[0].strip()
        amount = row[1].strip()
        dv = row[2].strip() if len(row) >= 3 else ""

        if not nutrient or nutrient.lower() in {
            "nutrition facts",
            "portion size",
            "amount per portion",
            "calories",
            "% daily value *",
        }:
            continue

        rows.append([nutrient, amount, dv])

    if rows:
        break

if rows:
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["nutrient", "amount", "dv"])
        writer.writerows(rows)
    print(f"CSV creado: {csv_path} con {len(rows)} filas")
else:
    print("No se encontró una tabla con encabezados Nutrient / Amount / DV.")