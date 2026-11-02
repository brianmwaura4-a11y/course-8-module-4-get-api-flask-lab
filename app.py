from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)


# Homepage route
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to the Product Catalogue API"
    }), 200


# Get all products or filter by category
@app.route("/products", methods=["GET"])
def get_products():
    category = request.args.get("category")

    if not category:
        return jsonify(products), 200

    category = category.strip().lower()

    filtered_products = [
        product for product in products
        if product["category"].lower() == category
    ]

    return jsonify(filtered_products), 200


# Get a product by ID
@app.route("/products/<int:id>", methods=["GET"])
def get_product_by_id(id):
    product = next(
        (product for product in products if product["id"] == id),
        None
    )

    if product is None:
        return jsonify({
            "error": "Product not found"
        }), 404

    return jsonify(product), 200


if __name__ == "__main__":
    app.run(debug=True)
