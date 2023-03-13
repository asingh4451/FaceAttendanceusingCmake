import streamlit as st
from st_function import st_button
import pickle as pk
import streamlit_authenticator as auth
import database as db
import pandas as pd
#from streamlit_webrtc import webrtc_streamer
#import subprocess
users=db.fetch_all_users()
usernames=[user["key"] for user in users]
names=[user["name"]for user in users]
passwords=[user["password"]for user in users]
names=[user["name"]for user in users]
passwords=[user["password"]for user in users]
st.header("Thapar  Face Attendance System")
authenticator=auth.Authenticate(names,usernames,passwords,"Firstpage","abcdef",cookie_expiry_days=3)
name,authentication_status,username=authenticator.login("Login","main")
Tea= {}
dat2=[]
data2=[]
for key in usernames:
    for value in names:
        Tea[key] = value
        names.remove(value)
        break
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://www.thapar.edu/images/noimage.jpg");
background-size: cover;
}
[data-testid="stHeader"]{
    background-colour: rgba(0,0,0,0);
}
[data-testid="stToolbar]{
    right:2rem;
}
</style>
"""
st.markdown(page_bg_img,unsafe_allow_html=True)
if authentication_status == False:
    st.error("Incorrect password or Username")
if authentication_status == None:
    st.error("Enter Username and Password")
if authentication_status:
    if(username[0:3]=="tea"):
        st.header("Welcome Teacher")
        response2=st.button("View Attendance of Current Class")
        if(response2==True):
                dat=pd.read_csv("Attendance.csv")
                st.table(dat)
        st.button("View My Classes")
    if(username[0:3]=="Mai"):
        st.header("Welcome Admin")
        response3=st.button("View Attendance of Current Class")
        if(response3==True):
                dat=pd.read_csv("Attendance.csv")
                st.table(dat)
        col1,col2,col3,col4=st.columns(4)
        with col1:
            st.button("Add Student to Current Class")
        with col2:
            st.button("Assign Teacher to Class")
        with col3:
            st.button("Add Student to a Class")
        with col4:
            response4=st.button("View teachers")
            if(response4==True):
                for i in Tea:
                    if(i[0:3]=="tea"):
                        dat2.append(Tea[i])
                data=pd.DataFrame(dat2)
            st.table(dat2)
    if(username[0:3]=="stu"):
        st.header("Welcome Student")
        response=st.button("Mark  Attendance")
        if(response==True):
            st_button("Mark my Attendance","http://127.0.0.1:5000")
        response2=st.button("View attendance")
        if(response2==True):
                dat=pd.read_csv("Attendance.csv")
                st.dataframe(dat)
authenticator.logout("Logout","main")
