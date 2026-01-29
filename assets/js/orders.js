const ordersContainer = document.getElementById("ordersContainer");

const orders = JSON.parse(localStorage.getItem("orders")) || [];

if (orders.length === 0) {
  ordersContainer.innerHTML = "<p>No orders found.</p>";
} else {
  orders.reverse().forEach(order => {
    const div = document.createElement("div");
    div.className = "product-box";

    div.innerHTML = `
      <h4>Order ID: ${order.id}</h4>
      <p><strong>Date:</strong> ${order.date}</p>
      <p><strong>Total:</strong> ₹${order.total}</p>
      <p><strong>Status:</strong> ${order.status}</p>
    `;

    ordersContainer.appendChild(div);
  });
}
