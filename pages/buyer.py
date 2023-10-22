import streamlit as st
from streamlit_card import card
from supabase import create_client, Client

url: str = 'https://dawdtngwbigpwxbzbadx.supabase.co'
key: str = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRhd2R0bmd3YmlncHd4YnpiYWR4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTc5MTkzNzIsImV4cCI6MjAxMzQ5NTM3Mn0.cwZUW05eQmjY9FH5XIirGdmCpMunABhwOmWheuc4lZQ'
supabase: Client = create_client(url, key)
st.set_page_config(layout="wide")

def main():

    st.markdown('<link rel="stylesheet" type="text/css" href="styles.css">', unsafe_allow_html=True)
    st.title("Chef Connect")
    word = st.selectbox("Type in a food", ["Select an Option", "Chicken Biryani", "Pizza", "Mac & Cheese", "Paneer Tikka Masala"], key="food")
    if (word == "Select an Option"):
        st.session_state.food = None

    response = supabase.table('foods').select("*").eq("name", word).execute()

    print(response)

    col1, col2 = st.columns([2, 3])  # Specify the number of columns as an integer (3).
    # for country in supabase.table('countries').select("*").execute().get('data'):
    #     print(country)
    #loop thru all countries
    # response = supabase.table('countries').select("*").execute()
    # print(response)
    if (st.session_state.food != None):
        with col1:
            if response:
                card(title=word,  # Replace the image URL with the actual URL.
                     text="Chef: ",
                     image="https://www.indianhealthyrecipes.com/wp-content/uploads/2021/12/chicken-biryani.jpg.webp",  # Replace with the actual image URL.
                     on_click=lambda: print("Clicked!"),
                     styles={
                        "card": {
                            "width": "300px",
                            "height": "300px",
                        },
                        "text": {
                            "font-family": "serif",
                        }
                     })
        with col2:
            card(title="Hello World!",
                 text="Some description",
                 image="http://placekitten.com/200/300",  # Replace with the actual image URL.
                 on_click=lambda: print("Clicked!"))
# Run

if __name__ == "__main__":
    main()