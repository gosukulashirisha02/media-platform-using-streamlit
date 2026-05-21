import streamlit as st 
from db_c import conn_obj,cursor_obj

login, signup=st.tabs(
    ["login","signup"]
)
cursor_obj.execute("show databases")
dbs=cursor_obj.fetchall()

for db in dbs:
    st.write(db)

with login:
    st.header("login")
    with st.form("login-forms"):
        email=st.text_input("Email")
        password=st.text_input("Password")
        btn=st.form_submit_button("Login")
    
    
with signup:
    st.header("signup")
    with st.form("signup-forms"):
        email=st.text_input("Email")
        password=st.text_input("Password")
        btn=st.form_submit_button("Signup")