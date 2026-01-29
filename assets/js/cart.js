function addToCart(name, price) {
  let cart = JSON.parse(localStorage.getItem("cart")) || [];

  cart.push({ name, price });

  localStorage.setItem("cart", JSON.stringify(cart));

  alert(name + " added to cart");
}

/* SHOW CART ITEMS */
function loadCart() {
  let cart = JSON.parse(localStorage.getItem("cart")) || [];
  let cartItemsDiv = document.getElementById("cart-items");
  let total = 0;

  if (!cartItemsDiv) return;

  cartItemsDiv.innerHTML = "";

  if (cart.length === 0) {
    cartItemsDiv.innerHTML = "<p>Your cart is empty.</p>";
    document.getElementById("cart-total").innerText = "";
    return;
  }

  cart.forEach((item, index) => {
    total += item.price;

    cartItemsDiv.innerHTML += `
      <div style="margin-bottom:15px;">
        <strong>${item.name}</strong> - ₹${item.price}
        <button onclick="removeItem(${index})" style="margin-left:10px;">
          Remove
        </button>
      </div>
    `;
  });

  document.getElementById("cart-total").innerText =
    "Total: ₹" + total;
}

/* REMOVE ITEM */
function removeItem(index) {
  let cart = JSON.parse(localStorage.getItem("cart")) || [];
  cart.splice(index, 1);
  localStorage.setItem("cart", JSON.stringify(cart));
  loadCart();
}

/* GO TO CHECKOUT */
function goToCheckout() {
  window.location.href = "checkout.html";
}

/* AUTO LOAD CART */
window.onload = loadCart;
