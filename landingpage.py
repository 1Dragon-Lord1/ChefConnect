import streamlit as st
from pages import seller as Seller
from pages import buyer as Buyer

# Create a function for the landing page
def landing_page():
    st.title("Chef Connect!")
    st.header("Are you a Seller or a Buyer?")

    # Embed a banner image
    banner_image = "banner.png"  # Replace with the path to your image
    st.image(banner_image, use_column_width=True)

    # Create buttons for Seller and Buyer
    if st.button("Seller"):
        # Redirect to the seller page when the "Seller" button is clicked
        st.experimental_set_query_params(role="seller")
    if st.button("Buyer"):
        # Redirect to the buyer page when the "Buyer" button is clicked
        st.experimental_set_query_params(role="buyer")

# Create a function for the seller page
def seller_page():
    st.title("Seller Page")
    # Link to seller.py in same directory
    # seller = Seller()
    # seller.seller_profile()
    # Add seller-related content and functionality here


# Create a function for the buyer page
def buyer_page():
    st.title("Buyer Page")
    # Link to buyer.py
    # buyer = Buyer()
    # buyer.buyer_profile()
    # Add buyer-related content and functionality here


# Main function
def main():
    # Check the query parameters to determine the user's role
    role = st.experimental_get_query_params().get("role")

    if role == "seller":
        seller_page()  # Redirect to the seller page
    elif role == "buyer":
        buyer_page()  # Redirect to the buyer page
    else:
        landing_page()  # Display the landing page by default

if __name__ == "__main__":
    main()