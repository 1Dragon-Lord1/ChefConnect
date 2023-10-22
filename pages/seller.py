import streamlit as st


# Define the Seller class
class Seller:
    def __init__(self, name, food_types, address, availability, profile_picture):
        self.name = name
        self.food_types = food_types
        self.address = address
        self.availability = availability
        self.profile_picture = profile_picture


# Create a function for the seller profile page
def seller_profile():
    st.title("Seller Profile")

    # Add a form for sellers to update their profile information
    st.header("Update Your Profile")

    # Input fields for seller information
    seller_name = st.text_input("Seller Name", value="JJ Pandit")
    food_types = st.text_input("Food Types (e.g., Indian, Asian)", value="Indian, Asian")
    address = st.text_area("Address", value="201 East 21st Street, Austin, USA")
    availability = st.selectbox("Availability for Delivery", ["Yes", "No"])

    # File uploader for profile picture
    profile_picture = st.file_uploader("Upload Profile Picture", type=["jpg", "png", "jpeg"])

    # Create a seller instance
    seller = Seller(seller_name, food_types, address, availability, profile_picture)

    # Save button to update the profile
    if st.button("Save Profile"):
        pass
    # Store the seller object in your database or data structure

    # Display current seller information
    st.header("Current Profile Information")
    st.write(f"Seller Name: {seller.name}")
    st.write(f"Food Types: {seller.food_types}")
    st.write(f"Address: {seller.address}")
    st.write(f"Availability for Delivery: {seller.availability}")

    # Display the profile picture if uploaded
    if seller.profile_picture:
        st.image(seller.profile_picture, caption="Profile Picture", use_column_width=True)


def menu_page():
    # This page should allow the seller to input details on the food they will make
    st.title("Menu Page")
    st.header("Update Your Menu")
    # Input fields for menu information
    menu_name = st.text_input("Menu Name", value="Menu Name")
    menu_description = st.text_input("Menu Description", value="Menu Description")
    menu_price = st.text_input("Menu Price", value="Menu Price")
    menu_picture = st.file_uploader("Upload Menu Picture", type=["jpg", "png", "jpeg"])
    # Create a menu instance
    # menu = Menu(menu_name, menu_description, menu_price, menu_picture)
    # # Save button to update the menu
    # if st.button("Save Menu"):
    #     pass
    # # Store the menu object in your database or data structure
    # # Display current menu information
    # st.header("Current Menu Information")
    # st.write(f"Menu Name: {menu.menu_name}")
    # st.write(f"Menu Description: {menu.menu_description}")
    # st.write(f"Menu Price: {menu.menu_price}")
    # # Display the menu picture if uploaded
    # if menu.menu_picture:
    #     st.image(menu.menu_picture, caption="Menu Picture", use_column_width=True)


# Main function
def main():
    st.sidebar.title("Seller Panel")
    page = st.sidebar.radio("Select a Page", ["Dashboard", "Profile", "Orders", "Settings"])

    if page == "Dashboard":
        # Add dashboard functionality
        pass
    elif page == "Profile":
        seller_profile()
    elif page == "Menu":
        menu_page()
    elif page == "Orders":
        # Add order management functionality
        pass
    elif page == "Settings":
        # Add settings functionality
        pass


if __name__ == "__main__":
    main()