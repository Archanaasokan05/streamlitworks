import streamlit as st
from library_db import BookListCreateRetrieveUpdateDelete

st.header("READ A SPECIFIC BOOK RECORD")
id=st.number_input("Enter Book ID:")
btn=st.button("Retrieve")
if btn:
    b = BookListCreateRetrieveUpdateDelete()
    record=b.retrieve(id)
    print(record)
    if record:
        st.write("Title:",record[1])
        st.write("Author:",record[2])
        st.write("Price:",record[3])
        st.write("Pages:",record[4])
        st.write("Languages:",record[5])
    else:
        print("NO RECORDS FOUND")
