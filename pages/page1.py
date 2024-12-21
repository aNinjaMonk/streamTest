import streamlit as st;

st.title("Page 1")
st.write("This is page 1")

st.button("Go to Page 2", on_click=lambda: st.page_link("pages/page2.py"))