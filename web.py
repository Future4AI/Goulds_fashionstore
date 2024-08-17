from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Sample product data
products = [
    {'id': 1, 'name': 'Jordan Air Max', 'sizes': [44], 'price': 500},
    {'id': 2, 'name': 'Prada Slide', 'sizes': [44], 'price': 150},
]

# In-memory cart storage (replace with database or session in production)
cart = {}

@app.route('/')
def home():
    return render_template('index.html', products=products)

@app.route('/cart', methods=['POST', 'GET'])
def cart():
    if request.method == 'POST':
        product_id = int(request.form['product_id'])
        size = int(request.form['size'])
        quantity = int(request.form['quantity'])

        product = next((p for p in products if p['id'] == product_id), None)
        if product and size in product['sizes']:
            cart_item = cart.get(product_id, {})
            cart_item[size] = cart_item.get(size, 0) + quantity
            cart[product_id] = cart_item
            return jsonify({'message': 'Product added to cart'})
        else:
            return jsonify({'error': 'Product or size not found'}), 400
    else:
        total_price = sum(sum(product['price'] * quantity for size, quantity in sizes.items()) for product_id, sizes in cart.items())
        return render_template('cart.html', cart=cart, total_price=total_price)

@app.route('/checkout')
def checkout():
    # Implement payment processing, order confirmation, etc.
    total_price = sum(sum(product['price'] * quantity for size, quantity in sizes.items()) for product_id, sizes in cart.items())
    return render_template('checkout.html', total_price=total_price)

if __name__ == '__main__':
    app.run(debug=True)
