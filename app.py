import streamlit as st

st.title("Media Platform")

login,signup=st.tabs(
    ["Login","Signup"]
)

with login:
    st.header("Login")
    with st.form("Login_forms"):
        email=st.text_input("Email")
        password=st.text_input("Password",type="password")
        btn=st.form_submit_button("Login")
        
        
with signup:
    st.header("Signup")
    with st.form("Signup_forms"):
        name=st.text_input("Name")
        email=st.text_input("Email")
        password=st.text_input("Password",type="password")
        btn=st.form_submit_button("SignUp")
    
        
        