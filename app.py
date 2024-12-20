import streamlit as st;
import pandas as pd;
import numpy as np;
from datetime import time, datetime;
import string;

def hello_world():
    st.title("Hello World")
    st.chat_message("user")
    st.write("Hello World again")
    prompt = st.chat_input("Enter your prompt")
    if prompt:
        st.chat_message("assistant")
        st.write(prompt)

def main():
    hello_world()

if __name__ == "__main__":
    main()