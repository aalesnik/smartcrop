from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about-us')
def about_us():
    return render_template('about-us.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/integration')
def integration():
    return render_template('integration.html')

@app.route('/main')
def main_page():
    return render_template('main.html')

@app.route('/product-details')
def product_details():
    return render_template('product-details.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/statistics')
def statistics():
    return render_template('statistics.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)