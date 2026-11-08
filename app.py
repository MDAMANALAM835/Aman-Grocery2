
from flask import Flask, render_template
import boto3
from botocore.exceptions import ClientError

app = Flask(__name__)

# AWS S3 settings
S3_BUCKET = "grocerybucket2026"
S3_REGION = "ap-southeast-2"

# Connect through EC2 IAM Role
s3 = boto3.client(
    "s3",
    region_name=S3_REGION
)

# Four grocery products
products = [
    {
        "name": "Apple",
        "category": "Fruits",
        "price": 120,
        "unit": "kg",
        "image_file": "apple.png"
    },
    {
        "name": "Banana",
        "category": "Fruits",
        "price": 60,
        "unit": "dozen",
        "image_file": "banana.png"
    },
    {
        "name": "Potato",
        "category": "Vegetables",
        "price": 30,
        "unit": "kg",
        "image_file": "potato.png"
    },
    {
        "name": "Tomato",
        "category": "Vegetables",
        "price": 40,
        "unit": "kg",
        "image_file": "tomato.png"
    }
]

@app.route("/")
def home():

    display_products = []

    for product in products:
        item = product.copy()

        try:
            item["image_url"] = s3.generate_presigned_url(
                "get_object",
                Params={
                    "Bucket": S3_BUCKET,
                    "Key": product["image_file"]
                },
                ExpiresIn=3600
            )

        except ClientError as error:
            print("S3 image error:", error)
            item["image_url"] = ""

        display_products.append(item)

    return render_template(
        "index.html",
        products=display_products
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )
