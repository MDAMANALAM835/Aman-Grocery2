
from flask import Flask, render_template

app = Flask(__name__)

S3_BASE_URL = "https://grocerybucket2026.s3.ap-southeast-2.amazonaws.com/"

products = [
    {"id": 1, "name": "Banana", "category": "Fruits", "price": 40, "unit": "dozen", "image_url": S3_BASE_URL + "banana.png"},
    {"id": 2, "name": "Apple", "category": "Fruits", "price": 120, "unit": "kg", "image_url": S3_BASE_URL + "apple.png"},
    {"id": 3, "name": "Tomato", "category": "Vegetables", "price": 35, "unit": "kg", "image_url": S3_BASE_URL + "tomato.png"},
    {"id": 4, "name": "Potato", "category": "Vegetables", "price": 30, "unit": "kg", "image_url": S3_BASE_URL + "potato.png"}
]

@app.route("/")
def home():
    return render_template("index.html", products=products)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
