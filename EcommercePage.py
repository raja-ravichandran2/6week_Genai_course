import streamlit as st
import pandas as pd

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="E-Commerce Application",
    page_icon="🛒",
    layout="wide"
)

# -------------------------------------------------
# Sample Product Data
# -------------------------------------------------

products = [

    {
        "id": 1,
        "name": "Apple iPhone 15",
        "category": "Mobiles",
        "price": 79999,
        "rating": 4.8
    },

    {
        "id": 2,
        "name": "Samsung Galaxy S24",
        "category": "Mobiles",
        "price": 69999,
        "rating": 4.6
    },

    {
        "id": 3,
        "name": "Sony Headphones",
        "category": "Electronics",
        "price": 4999,
        "rating": 4.5
    },

    {
        "id": 4,
        "name": "HP Laptop",
        "category": "Laptops",
        "price": 65000,
        "rating": 4.4
    },
    {
        "id": 5,
        "name": "Boat Smart Watch",
        "category": "Wearables",
        "price": 2999,
        "rating": 4.2
    },
    {
        "id": 6,
        "name": "Apple SE Smart Watch",
        "category": "Wearables",
        "price": 29999,
        "rating": 4.4
    },
    {
        "id": 7,
        "name": "Samsung Galaxy S4 Smart Watch",
        "category": "Wearables",
        "price": 59999,
        "rating": 4.4
    },

]

# -------------------------------------------------
# Session State for Cart
# -------------------------------------------------

if "cart" not in st.session_state:
    st.session_state.cart = []

# -------------------------------------------------
# Header
# -------------------------------------------------

st.title("🛒 E-Commerce Application")

st.write("Welcome to Raja Online Shopping")

# -------------------------------------------------
# Sidebar Filters
# -------------------------------------------------

st.sidebar.header("🔍 Filter Products")

categories = ["All"] + list(
    set(product["category"] for product in products)
)

selected_category = st.sidebar.selectbox(
    "Select Category",
    categories
)

search_text = st.sidebar.text_input(
    "Search Product"
)

# -------------------------------------------------
# Filter Logic
# -------------------------------------------------

filtered_products = []

for product in products:

    if selected_category != "All":

        if product["category"] != selected_category:
            continue

    if search_text.lower() not in product["name"].lower():
        continue

    filtered_products.append(product)

# -------------------------------------------------
# Display Products
# -------------------------------------------------

st.subheader("🛍 Available Products")

cols = st.columns(2)

for index, product in enumerate(filtered_products):

    with cols[index % 2]:

        st.markdown("----")

        st.subheader(product["name"])

        st.write(f"📂 Category: {product['category']}")

        st.write(f"💰 Price: ₹{product['price']}")

        st.write(f"⭐ Rating: {product['rating']}")

        if st.button(
            f"Add to Cart - {product['id']}"
        ):

            st.session_state.cart.append(product)

            st.success(
                f"{product['name']} added to cart"
            )

# -------------------------------------------------
# Cart Section
# -------------------------------------------------

st.markdown("---")

st.header("🛒 Shopping Cart")

if len(st.session_state.cart) == 0:

    st.warning("Cart is empty")

else:

    cart_df = pd.DataFrame(
        st.session_state.cart
    )

    st.dataframe(cart_df)

    total_price = cart_df["price"].sum()

    st.subheader(
        f"💵 Total Amount: ₹{total_price}"
    )

    if st.button("Place Order"):

        st.success(
            "✅ Order Placed Successfully!"
        )

        st.balloons()

        st.session_state.cart = []

# -------------------------------------------------
# Footer
# -------------------------------------------------

st.markdown("---")

st.write("🚀 Built using Streamlit")