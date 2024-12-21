import streamlit as st;

st.title("Page 2")
st.write("This is page 2")

st.button("Go to Page 1", on_click=lambda: st.navigate("page1"))