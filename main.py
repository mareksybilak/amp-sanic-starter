from sanic import Sanic
from sanic.response import json
from panel import admin_panel
from sanic_jinja2 import SanicJinja2


app = Sanic()
app.static('/static', './static')
jinja = SanicJinja2(app)

@app.route("/")
@jinja.template('landing.amp.html')
async def landing(request):
    return {"hello": "world"}

@app.route("/product-listing")
@jinja.template('product-listing.amp.html')
async def product_listing(request):
    return {"hello": "world"}

@app.route('/product-details', name='product')
@jinja.template('product-details.amp.html')
async def product_details(request):
    return {'product_id':'product_id'}

@app.route("/blog-listing")
@jinja.template('blog-listing.amp.html')
async def blog_listing(request):
    return {"hello": "world"}

@app.route("/blog-article")
@jinja.template('blog-article.amp.html')
async def blog_article(request):
    return {"hello": "world"}

@app.route("/cart")
@jinja.template('cart.amp.html')
async def cart(request):
    return {"hello": "world"}

@app.route("/checkout")
@jinja.template('checkout.amp.html')
async def checkout(request):
    return {"hello": "world"}

@app.route("/checkout-success")
@jinja.template('checkout-success.amp.html')
async def checkout_success(request):
    return {"hello": "world"}

@app.route("/contact")
@jinja.template('contact.amp.html')
async def contact(request):
    return {"hello": "world"}

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)