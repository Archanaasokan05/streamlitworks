import streamlit as st
from library_db import BookListCreateRetrieveUpdateDelete

st.header("READ ALL BOOK RECORD")
b=BookListCreateRetrieveUpdateDelete()
records=b.list()
print("Hello")
print(records)
st.table(records)