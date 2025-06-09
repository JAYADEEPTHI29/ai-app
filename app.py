from flask import Flask, render_template, jsonify
import json
from description_generator.generator import generate_description

app = Flask(__name__)

# Load products from JSON
with open('products.json') as f:
    products = json.load(f)

# Route: Homepage - product list
@app.route('/')
def home():
    return render_template('home.html', products=products)

# Route: Product detail page
@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = products[product_id]
    description_data = generate_description(product)
    return render_template('product_detail.html', product=product, description=description_data)

if __name__ == '__main__':
    app.run(debug=True)
