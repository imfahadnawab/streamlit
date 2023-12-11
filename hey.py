import streamlit as sm 


sm.text_input("Enter Name")
s=sm.radio("Are you a student",options=["Yes","No"],index=0)
m=sm.text_input("Marks Obtained")
tm=sm.text_input("Enter Maximum Marks")
try:
    k=(int(m)//int(tm))*100
    if k>=75:
        sm.write("Your Package is 10 LPA")
    else:
        sm.write("You're Not Selected")
except ValueError:
    sm.write("Please enter valid numeric values for Marks Obtained and Maximum Marks.")

sm.balloons()