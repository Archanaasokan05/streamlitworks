import streamlit as st
from library_db import BookListCreateRetrieveUpdateDelete

# data = (title, author, price, pages, language)

st.header("ADD NEW BOOK RECORD")
title=st.text_input("Enter book Title:")
author=st.text_input("Author Name:")
price=st.number_input("Price:")
pages=st.number_input("No. of Pages:")
language=st.text_input("Language:")
btn=st.button("ADD BOOK")
if btn:
    b=BookListCreateRetrieveUpdateDelete()
    b.create(title, author, price, pages, language)
    st.success("RECORD CREATED SUCCESSFULLY")