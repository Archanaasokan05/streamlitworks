import streamlit as st
from library_db import BookListCreateRetrieveUpdateDelete

tab1,tab2,tab3,tab4,tab5=st.tabs(['ADD','VIEW','RETRIEVE','DELETE','UPDATE'])
b=BookListCreateRetrieveUpdateDelete()

with tab1:
    # st.title("ADD")
    st.header("ADD NEW BOOK RECORD")
    title = st.text_input("Enter Book Title:")
    author = st.text_input("Author Name:")
    price = st.number_input("Price for Book for Book:")
    pages = st.number_input("Number of Pages:")
    language = st.text_input("Language of the Book:")
    btn = st.button("ADD BOOK")
    if btn:
        b = BookListCreateRetrieveUpdateDelete()
        b.create(title, author, price, pages, language)
        st.success("RECORD CREATED SUCCESSFULLY")

with tab2:
    # st.title("VIEW")
    st.header("READ ALL BOOK RECORD")
    b = BookListCreateRetrieveUpdateDelete()
    records = b.list()
    print(records)
    st.table(records)

with tab3:
    st.header("READ A SPECIFIC BOOK RECORD")
    id = st.number_input("Enter Book ID:")
    btn = st.button("RETRIEVE")
    if btn:
        b = BookListCreateRetrieveUpdateDelete()
        record = b.retrieve(id)
        print(record)
        if record:
            st.write("Title:", record[1])
            st.write("Author:", record[2])
            st.write("Price:", record[3])
            st.write("Pages:", record[4])
            st.write("Languages:", record[5])
        else:
            st.error("NO RECORDS FOUND")

with tab4:
    # st.title("DELETE")
    st.header("DELETE BOOK RECORD")
    # id = st.number_input("Enter Book ID:",key="delete_id")     ## In Streamlit, we use a unique key for repeated widgets
    id = st.number_input("Enter Book Id:")                       ## so that Streamlit can identify and manage each widget
                                                                 ## separately without causing a duplicate element ID error.
    btn = st.button("DELETE RECORD")
    if btn:
        b = BookListCreateRetrieveUpdateDelete()
        status = b.delete(id)
        if status:
            st.success("RECORD DELETED SUCCESSFULLY")
        else:
            st.error("RECORD NOT FOUND")

with tab5:
    # st.title("UPDATE")
    st.header("UPDATE BOOK RECORD")
    id = st.number_input("Enter Book ID for Update:")
    title = st.text_input("Enter Book title:")
    author = st.text_input("Enter Author Name:")
    price = st.number_input("Price:")
    pages = st.number_input("No. of Pages:")
    language = st.text_input("Language:")
    btn = st.button("UPDATE BOOK")
    if btn:
        b = BookListCreateRetrieveUpdateDelete()
        status = b.update(title, author, price, pages, language, id)
        if status:
            st.success("UPDATE SUCCESSFULLY")
        else:
            st.error("NO RECORD FOUND")
