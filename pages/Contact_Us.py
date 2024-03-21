import streamlit as st
from send_email import send_email
import pandas

df = pandas.read_csv("topics.csv")
st.header("Contact Me")


with st.form(key="email_forms"):
    user_email = st.text_input("Your email  address")
    option = st.selectbox(
        'What topic do you want to discuss',
        df["topic"]
    )
    raw_message = st.text_area("Your message here")
    message = f"""
        Subject: Email from {user_email}
        Topic {option}
        {raw_message}
     """
    button = st.form_submit_button("Submit")
    if button:
        send_email(message, user_email)
        st.info("Your email was sent successfully")
