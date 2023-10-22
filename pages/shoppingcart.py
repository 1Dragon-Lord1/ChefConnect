import streamlit as st

#Create a class to represent a product
class Product:
    def init(self, name, maker, quantity, price, delivery_date, delivery_method, image_url):
        self.name = name
        self.maker = maker
        self.quantity = quantity
        self.price = price
        self.delivery_date = delivery_date
        self.delivery_method = delivery_method
        self.image_url = image_url

#Create a list of sample products
products = [
    Product("Product 1", "Manufacturer A", 2, 10.99, "2023-10-30", "Express", "image1.jpg"),
    Product("Product 2", "Manufacturer B", 1, 5.99, "2023-11-05", "Standard", "image2.jpg"),
    Product("Product 3", "Manufacturer C", 3, 15.99, "2023-11-10", "Express", "image3.jpg"),
]

#Create the shopping cart page
st.title("Shopping Cart")

#Display product details in a loop
for product in products:
    st.write(f"### {product.name}")
    st.image(product.image_url, width=100)
    st.write(f"Aunty: {product.maker}")
    st.write(f"Quantity: {product.quantity}")
    st.write(f"Price: ${product.price:.2f}")
    st.write(f"Delivery Time: {product.delivery_date}")
    st.write(f"Delivery Method: {product.delivery_method}")
    st.write("---")

#Calculate and display the total price
total_price = sum(product.price * product.quantity for product in products)
st.write(f"Total Price: ${total_price:.2f}")