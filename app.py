from flask import Flask, render_template, request

app = Flask(__name__)

products = [
    {"name": "T-Shirt", "price": 499},
    {"name": "Shoes", "price": 1999},
    {"name": "Watch", "price": 1499},
    {"name": "Bag", "price": 999}
]

cart = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/products")
def products_page():
    return render_template("products.html", products=products)

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        print("Name:", name)
        print("Email:", email)

        return "Registration Successful"

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        print("Email:", email)

        return "Login Successful"

    return render_template("login.html")

@app.route("/add_to_cart/<int:product_id>")
def add_to_cart(product_id):

    product = products[product_id]
    cart.append(product)

    return "Product Added To Cart"

@app.route("/cart")
def view_cart():

    return render_template(
        "cart.html",
        cart=cart
    )
@app.route("/checkout")
def checkout():
    return render_template("checkout.html")
@app.route("/order_success")
def order_success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
