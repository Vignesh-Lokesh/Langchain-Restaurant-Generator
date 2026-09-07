import streamlit as st
import langchain_helper

st.title("🍽️ Restaurant Name Generator")

# Sidebar for cuisine selection
cuisine = st.sidebar.selectbox(
    "Pick a Cuisine",
    ("Indian", "Italian", "Mexican", "Arabic", "American")
)

if cuisine:
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)
    
    # Display restaurant name
    st.header(response['restaurant_name'].strip())

    # Display menu items
    st.subheader("Menu Items")
    for item in response['menu_items']:
        st.write("-", item)
