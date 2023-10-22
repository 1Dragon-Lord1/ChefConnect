import streamlit as st
from streamlit_card import card
from streamlit_elements import elements, mui, html
import requests
from supabase import create_client, Client
from PIL import Image
import streamlit as st
import base64
#
# def card_with_image_and_paragraph(image_url, paragraph_text):
#     # Create a container for the card
#     card_container = st.container()
#
#     # Use beta_columns to create two columns
#     image_column, text_column = st.columns([1, 2])
#
#     # In the first column, display the image
#     with image_column:
#         # st.image(image_url, styles={
#         #         "card": {
#         #             "width": "500px",
#         #             "height": "500px",
#         #         },
#         #         "text": {
#         #             "font-family": "serif",
#         #         }
#         #      })
#         st.image(image_url, use_column_width=True)
#
#     # In the second column, display the paragraph
#     with text_column:
#         st.write(paragraph_text)

# Example usage


url: str = 'https://dawdtngwbigpwxbzbadx.supabase.co'
key: str = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRhd2R0bmd3YmlncHd4YnpiYWR4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTc5MTkzNzIsImV4cCI6MjAxMzQ5NTM3Mn0.cwZUW05eQmjY9FH5XIirGdmCpMunABhwOmWheuc4lZQ'
supabase: Client = create_client(url, key)
st.set_page_config(layout="wide")

def main():

        # mui.collapse(in=True)
        # > Syntax error: 'in' is a Python keyword:
    with elements("Title"):
        html.p("Chef Connect", style={"font-size": "50px", "font-family": "serif", "text-align": "center"})
        html.hr()
    # st.title("Chef Connect")
    word = st.selectbox("Type in a food", ["Select an Option", "Chicken", "Chicken Biryani", "Pizza", "Mac & Cheese", "Paneer Tikka Masala", "Tofu"])
    with elements("Card"):
        with html.div(label = "flex-container", css = {"display" : "flex", "flex-direction" : "row", "background-color" : "red"}):
            with html.div(label="headshot", css = {"background-color" : "blue", "margin-bottom" : "0px", "flex" : "2"}):
                html.img(src="https://placekitten.com/200/300")
            with html.div(label="stuff", css = {"flex" : 10}):
                html.div("Hii")
            with html.div(label="image", css = {"flex" : "2"}):
                html.img(src="https://placekitten.com/200/300")

    with elements("NiceCard"):
        with html.div(label="flex-container",
                      css={"display": "flex", "flex-direction": "row", "background-color": "red"}):
            with mui.Card(sx = {"width" : 320}):
                with html.div:
                    mui.Typography("Yosemite National Park", level = "title-lg")
                    mui.Typography("April 24 to May 02, 2021", level = "body-sm")
                html.img(src="https://placekitten.com/200/300")
                with mui.CardContent(orientation = "horizontal"):
                    with html.div:
                        mui.Typography("Price:", level='body-xs')
                        mui.Typography("$2,500", fontSize="lg", fontWeight="lg")
                mui.Button(variant="solid", size="md", color="primary", sx = {"ml" : 'auto',
                                                                                   'alignSelf':'center',
                                                                                   'fontWeight':600})

    # print(word)
    #convert all spaces to _ in word
    word = word.replace(" ", "_")
    food_image = requests.get("https://www.themealdb.com/api/json/v1/1/search.php?s=" + word).json()["meals"][0]["strMealThumb"]
    # print(food_image)
    response = supabase.table('foods').select("*").eq("name", word).execute()

    # response = supabase.table('countries').select("*").eq("name", "United States").execute()
    # print("RESPONSE", response)
    # col1, col2, col3 = st.columns([4, 3, 2])  # Specify the number of columns as an integer (3).
    # with col1:
    #     card(title=word,  # Replace the image URL with the actual URL.
    #          text="",
    #          image=food_image,  # Replace with the actual image URL.
    #          on_click=lambda: print("Clicked!"),
    #          styles={
    #             "card": {
    #                 "width": "500px",
    #                 "height": "500px",
    #             },
    #             "text": {
    #                 "font-family": "serif",
    #             }
    #          })
    # with col2:
    #     with elements("properties"):

            # You can add properties to elements with named parameters.
            #
            # To find all available parameters for a given element, you can
            # refer to its related documentation on mui.com for MUI widgets,
            # on https://microsoft.github.io/monaco-editor/ for Monaco editor,
            # and so on.
            #
            # <Paper elevation={3} variant="outlined" square>
            #   <TextField label="My text input" defaultValue="Type here" variant="outlined" />
            # </Paper>
            #add a mui div
            # with html.div(label = "flex-container", sx = {"display" : "flex", "flex-direction" : "row", "background-color" : "red"}):
            #     with html.div(label="headshot", sx = {"background-color" : "blue"}):
            #         mui.Avatar(src="https://placekitten.com/200/300")
            #     with html.div(label="stuff"):
            #         with mui.Card:
            #             with mui.CardActionArea:
            #                 mui.CardMedia(image="chef_profile_pics/Kevin.jpg", height="140", component="img")
            #             with mui.CardContent:
            #                 mui.Typography("Hello world", variant="h5", component="h2")
            #                 mui.Typography("This is a card", variant="body2", component="p")
            #     # mui.TextField(
            #     #     label="My text input",
                #     defaultValue="Type here",
                #     variant="outlined",
                # )
            # with mui.Box(
            #     "Some text in a styled box",
            #     sx={
            #         "bgcolor": "background.paper",
            #         "boxShadow": 1,
            #         "borderRadius": 2,
            #         "p": 2,
            #         "minWidth": 300,
            #     }
            # ):
                # mui.Typography("Some text inside the box")
            # with mui.Box("Hello world", sx = {"display" : "flex", "flex-direction" : "row",}):
            #     mui.Avatar(src="https://placekitten.com/200/300")

        #
        # # check if response is not empty
        # if len(response.data) > 0:
        #     for seller in response.data:
        #         # stuff = supabase.table('sellers').select('id, foods(id)').execute()
        #         # stuff = supabase.table('foods').select('seller_id, sellers(*)').eq('sellers.id', seller['seller_id']).execute()
        #         stuff = supabase.table('sellers').select('*').eq('name', "Sahil").execute()
        #         print("STUFF", stuff)
        #         print("SELLER")
        #         print(seller)
        #         seller_name = supabase.table('sellers').select('*').eq('id', seller['seller_id']).execute()
        #         print("SELLER_NAME", seller_name.data[0]['name'])
                # print(seller_name.data[0]['name'])
                # image = Image.open('Emerald.jpg')

                # card(title=seller_name.data[0]['name'],
                #      text="Some description",
                #      #retrive from directorty
                #      image='https://ibb.co/4YCpTjh',  # Replace with the actual image URL.
                #      on_click=lambda: print("Clicked!"),
                #      key = seller['seller_id'],
                #      styles={
                #          "card": {
                #              "width": "200px",
                #              "height": "300px",
                #              "border-radius": "60px",
                #              "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
                #              "column-gap": "100px",
                #          },
                #          "text": {
                #              "font-family": "serif",
                #          }
                #      }
                #      )
                # with col3:
                #     card(title="a",
                #          text="Some description",
                #          # retrive from directorty
                #          image='https://ibb.co/4YCpTjh',  # Replace with the actual image URL.
                #          on_click=lambda: print("Clicked!"),
                #          key=seller['seller_id'] + '1',
                #          styles={
                #              "card": {
                #                  "width": "300px",
                #                  "height": "300px",
                #                  "border-radius": "60px",
                #                  "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
                #                  #make no
                #              },
                #              "text": {
                #                  "font-family": "serif",
                #              }
                #          }
                #          )

# Run
# card_with_image_and_paragraph("https://placekitten.com/200/300", "This is a custom card with an image on the left and text on the right.")

if __name__ == "__main__":
    main()
