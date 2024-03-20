import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email  address")
    subject = st.text_input("Subject")
    raw_message = st.text_area("Your message here")
    message = f"{raw_message}"
    button = st.form_submit_button("Submit")
    if button:
        send_email(message, user_email)
        st.info("Your email was sent successfully")
