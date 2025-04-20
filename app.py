
from flask import Flask, request, render_template, redirect, url_for, session
import csv
import os
from datetime import datetime

app = Flask(__name__)

LOG_FILE = 'traffic_log.csv'

# Log traffic to CSV
def log_traffic(endpoint):
    log_data = [
        request.remote_addr,
        request.user_agent.string,
        endpoint,
        request.method,  # Add HTTP method (GET, POST, etc.)
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ]
    file_exists = os.path.isfile(LOG_FILE)
    with open(LOG_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['IP Address', 'User Agent', 'Endpoint', 'Method', 'Timestamp'])
        writer.writerow(log_data)

# Routes to log traffic

@app.route('/')
def home():
    log_traffic('/')
    return render_template('home.html')

@app.route('/products')
def show_products():
    log_traffic('/products')
    return render_template('products.html', products=["Product A", "Product B", "Product C"])

@app.route('/add-to-cart', methods=['POST'])
def add_to_cart():
    product = request.form['product']
    if 'cart' not in session:
        session['cart'] = []
    session['cart'].append(product)
    session.modified = True  # Required to update session
    log_traffic('/add-to-cart')  # Log POST request for add-to-cart
    return redirect(url_for('show_cart'))

@app.route('/cart')
def show_cart():
    log_traffic('/cart')
    cart = session.get('cart', [])
    return render_template('cart.html', cart=cart)

@app.route('/signup')
def signup():
    log_traffic('/signup')
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)

