from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = "namahvastra_secret_key"

# ---------------- PRODUCT DATA ----------------
products = {
    1: {
        "id": 1,
        "name": "Kanchipuram Silk Saree",
        "price": 4999,
        "fabric": "Pure Silk",
        "description": "Traditional Kanchipuram silk saree with rich zari work.",
        "image": "saree1.jpg"
    },
    2: {
        "id": 2,
        "name": "Banarasi Saree",
        "price": 3499,
        "fabric": "Silk Blend",
        "description": "Elegant Banarasi saree ideal for festive wear.",
        "image": "saree2.jpg"
    },
    3: {
        "id": 3,
        "name": "Organza Party Saree",
        "price": 2999,
        "fabric": "Organza",
        "description": "Lightweight organza saree for parties.",
        "image": "saree3.jpg"
    }
}

# ---------------- HOME ----------------
@app.route("/")
def home():
    return render_template("index.html")

# ---------------- SHOP ----------------
@app.route("/shop")
def shop():
    return render_template("shop.html", products=products)

# ---------------- PRODUCT ----------------
@app.route("/product/<int:id>")
def product(id):
    return render_template("product.html", product=products[id])

# ---------------- ADD TO CART ----------------
@app.route("/add_to_cart/<int:id>", methods=["POST"])
def add_to_cart(id):
    if "cart" not in session:
        session["cart"] = {}

    cart = session["cart"]
    cart[str(id)] = cart.get(str(id), 0) + 1
    session["cart"] = cart

    return redirect(url_for("cart"))

# ---------------- CART ----------------
@app.route("/cart")
def cart():
    cart_items = []
    total = 0

    if "cart" in session:
        for id, qty in session["cart"].items():
            product = products[int(id)]
            subtotal = product["price"] * qty
            total += subtotal

            cart_items.append({
                "product": product,
                "quantity": qty,
                "subtotal": subtotal
            })

    return render_template("cart.html", cart_items=cart_items, total=total)

# ---------------- REMOVE ITEM ----------------
@app.route("/remove/<int:id>")
def remove(id):
    session["cart"].pop(str(id), None)
    return redirect(url_for("cart"))

# ---------------- CHECKOUT ----------------
@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    if "cart" not in session or not session["cart"]:
        return redirect(url_for("shop"))

    cart_items = []
    total = 0

    for id, qty in session["cart"].items():
        product = products[int(id)]
        subtotal = product["price"] * qty
        total += subtotal

        cart_items.append({
            "product": product,
            "quantity": qty,
            "subtotal": subtotal
        })

    if request.method == "POST":
        name = request.form["name"]
        phone = request.form["phone"]
        address = request.form["address"]

        # Order confirmed (payment later)
        session.pop("cart")

        return f"""
        <h2>Thank you, {name}!</h2>
        <p>Your order has been placed successfully.</p>
        <p>Total Amount: ₹{total}</p>
        <a href="/shop">Continue Shopping</a>
        """

    return render_template(
        "checkout.html",
        cart_items=cart_items,
        total=total
    )

# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)
