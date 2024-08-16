async function addToCart(productId, size, quantity) {
  try {
    const response = await fetch('/cart', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        product_id: productId,
        size: size,
        quantity: quantity
      })
    });

    const data = await response.json();

    if (response.ok) {
      // Handle success, e.g., update cart display, show success message
      console.log('Product added to cart:', data);
    } else {
      // Handle error, e.g., display error message to user
      console.error('Error adding product to cart:', data.error);
      // You can implement specific error handling based on error codes or messages
    }
  } catch (error) {
    console.error('Network error:', error);
    // Handle network errors, e.g., show a retry message
  }
}