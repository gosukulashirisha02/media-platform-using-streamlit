import streamlit as st
from db_c import conn_obj,cursor_obj

st.title("Media Platform")

login,signup=st.tabs(
    ["Login","Signup"]
)
cursor_obj.execute("show databases")
dbs=cursor_obj.fetchall()
for db in dbs:
    st.write(db)

cursor_obj.execute("show tables")
dbs=cursor_obj.fetchall() 
for db in dbs:
    st.write(db)


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
        

        
        