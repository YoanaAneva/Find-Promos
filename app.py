import streamlit as st
from services.search import search_supermarkets
import base64
import os

# convert local files to base64 string so they can be embedded into the html
def image_to_base64(path):
    if not os.path.exists(path):
        return None
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# render the card component of each product
def render_offer_card(offer):
    with st.container():
        image_src = offer["image_src"]
        if not image_src :
            b64 = image_to_base64("assets/no-photo.jpg")
            image_src = f"data:image/png;base64,{b64}"

        st.markdown(
            f"""
            <div style="
            width: 80%;
            height: 20rem;
            overflow: hidden;
            border-radius: 6px;                
            display: flex;
            justify-content: center;
            align-items: center;
            margin-bottom: 1rem;
            margin-top: 1rem;
            background-color: white;">
                <img src="{image_src}" style="
                max-width: 100%;
                max-height: 100%;
                object-fit: contain;">
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(f"** {offer['supermarket']}**")
        st.markdown(f"### {offer['title']}")

        if offer["quantity"] :
            st.markdown(f"<span> {offer['quantity']} </span>", unsafe_allow_html=True)

        if offer["old_price_bgn"]:
            st.markdown(
                f"""<span style='color:gray;text-decoration:line-through;'>
                    {offer['old_price_bgn']} ({offer['old_price_eur']})
                </span>""",
                unsafe_allow_html=True
            )

        if offer["is_two_for_one"] :
            st.markdown("##1+1 Две на цената на едно")

        st.markdown(f"### {offer['price_bgn']} ({offer['price_eur']})")

        if offer["period"] :
            st.markdown(offer['period'])

def display_offers_as_cards(offers, cards_per_row=3):
    rows = [
        offers[i:i + cards_per_row]
        for i in range(0, len(offers), cards_per_row)
    ]

    for row in rows:
        cols = st.columns(cards_per_row)
        for col, offer in zip(cols, row):
            with col:
                render_offer_card(offer)


st.set_page_config(
    page_title = "Find promos",
    layout = "wide"
)

st.title("Търсене на промоции")

query = st.text_input("Въведи продукт", placeholder="Търсене")

if st.button("Търси") and query:
    with st.spinner("Проверка на супермаркети..."):
        results = search_supermarkets(query)

    if not results:
        st.warning("Няма намерени оферти")
    else:
        display_offers_as_cards(results)