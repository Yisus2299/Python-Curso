from flask import Flask, request, render_template
from PIL import Image
from collections import Counter

app = Flask(__name__)

def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(*rgb)

def extract_top_colors(image_file, top=10):
    image = Image.open(image_file).convert("RGB")
    image = image.resize((200, 200), Image.LANCZOS)
    image = image.quantize(colors=64, method=2)
    palette = image.getpalette()
    color_counts = image.getcolors(200 * 200)

    if not color_counts:
        return []

    results = []
    for count, palette_index in color_counts:
        r = palette[palette_index * 3]
        g = palette[palette_index * 3 + 1]
        b = palette[palette_index * 3 + 2]
        results.append((count, (r, g, b)))

    results.sort(reverse=True, key=lambda x: x[0])
    top_colors = [rgb_to_hex(rgb) for _, rgb in results[:top]]
    return top_colors

@app.route("/", methods=["GET", "POST"])
def index():
    colors = []
    filename = None
    if request.method == "POST":
        uploaded = request.files.get("image")
        if uploaded and uploaded.filename:
            colors = extract_top_colors(uploaded, top=10)
            filename = uploaded.filename
    return render_template("index.html", colors=colors, filename=filename)

if __name__ == "__main__":
    app.run(debug=True)