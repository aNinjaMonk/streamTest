import streamlit as st;
import pandas as pd;
import numpy as np;
import altair as alt;
from datetime import time, datetime;
import string;

if "count" not in st.session_state:
    st.session_state.count = 0

def hello_world():
    st.title("Hello World")
    st.chat_message("user")
    st.write("Hello World again")
    prompt = st.chat_input("Enter your prompt")
    if prompt:
        st.chat_message("assistant")
        st.write(prompt)
    st.file_uploader("Upload a file");

@st.cache_data
def load_data():
    df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/uber-rides-data1.csv")
    return df

def increment():
    st.session_state.count += 1

def decrement():
    st.session_state.count -= 1

def counter():
    st.title("Counter")
    st.button("Increment", on_click=increment)
    st.button("Decrement", on_click=decrement)
    st.write(st.session_state.count)

def form():
    with st.form("my_form"):
        st.write("Inside the form")
        slider_val = st.slider("Form slider")
        st.write(slider_val)
        color = st.selectbox("Select a color", ["red", "blue", "green"])
        st.write(color)
        date = st.date_input("Select a date")
        st.write(date)
        time = st.time_input("Select a time")
        st.write(time)
        st.text_input("Enter your name")
        st.text_area("Enter your message")
        st.number_input("Enter your age")
        st.number_input("Enter your height", step=0.05)
        st.form_submit_button("Submit")

@st.fragment (run_every="1s")
def fragment_fn():
    st.write("I am a Timer")
    st.write(datetime.now())

def chart():
    df = load_data()
    chart = alt.Chart(df).mark_line().encode(
        x="Lat",
        y="Lon"
    )
    st.altair_chart(chart)

def main():
    df = load_data()
    st.dataframe(df)
    #df = st.button("Load Data", on_click=load_data)
    #st.write(df)
    counter()
    #form()
    fragment_fn()
    chart()
    df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
    })
    st.dataframe(df)



if __name__ == "__main__":
    main()