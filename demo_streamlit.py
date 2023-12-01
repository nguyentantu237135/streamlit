import streamlit as st
import time

with st.spinner("Chờ xíu..."):
    time.sleep(3)
st.success('Xong')
ten = st.text_input("Nhập vào tên của bạn: ") 
click = st.button("Nhấn vào đây")
if click:
    st.write("Tên của bạn là: ", ten, "chó điên")

