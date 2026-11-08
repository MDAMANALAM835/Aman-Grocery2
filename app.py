
from flask import Flask, render_template
import boto3
from botocore.exceptions import ClientError

app = Flask(__name__)

# AWS S3 configuration
S3_BUCKET = "grocerybucket2026"
S3_REGION = "ap-southeast-2"

# Connect using EC2 IAM Role
s3 = boto3.client(
    "s3",
    region_name=S3_REGION
)

# Generate secure temporary image URLs
def get_image_url(filename):
    try:
        return s3.generate_presigned_url(
            "get_object",
            Params={
                "Bucket": S3_BUCKET,
                "Key": filename
            },
            ExpiresIn=3600
        )
    except ClientError as e:
        print("S3 Error:", e)
        return ""

@app.route("/")
def home():

    image_urls = {
        "apple": get_image_url("apple.png"),
        "banana": get_image_url("banana.png"),
        "potato": get_image_url("potato.png"),
        "tomato": get_image_url("tomato.png")
    }

    return render_template(
        "index.html",
        image_urls=image_urls
    )

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )
