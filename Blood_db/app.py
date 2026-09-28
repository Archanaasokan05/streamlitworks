import streamlit as st
from blood_db import DonarCRUD

tab1,tab2,tab3,tab4,tab5=st.tabs(['ADD','VIEW','RETRIEVE','DELETE','UPDATE'])
b=DonarCRUD()

# ADD
with tab1:
    st.header("ADD NEW DONAR RECORD")
    name = st.text_input("Enter Donar Name:")
    bloodgroup = st.text_input("Enter Blood Group:")
    phone = st.text_input("Phone:")
    city = st.text_input("City:")
    last_donation = st.date_input("Last Donation:")
    btn = st.button("ADD DONAR")
    if btn:
        b = DonarCRUD()
        b.post(name,bloodgroup,phone,city,last_donation)
        st.success("RECORD CREATED SUCCESSFULLY")

# VIEW
with tab2:
    st.header("READ ALL DONAR RECORD")
    b = DonarCRUD()
    records = b.get()
    print(records)
    if records:
        st.table(records)
    else:
        st.error("NO RECORDS FOUND")

# RETRIEVE
with tab3:
    st.header("READ A SPECIFIC DONAR RECORD")
    id = st.number_input("Enter Donar ID for Retrieve:")
    btn = st.button("Retrieve")
    if btn:
        b = DonarCRUD()
        record = b.retrieve(id)
        if record:
            st.write("Name:", record[1])
            st.write("Blood Group:", record[2])
            st.write("Phone:", record[3])
            st.write("City:", record[4])
            st.write("Last Donation:", record[5])
        else:
            st.error("NO RECORDS FOUND")

# DELETE
with tab4:
    st.header("DELETE DONAR RECORD")
    id = st.number_input("Enter Donar ID for Delete:")
    btn = st.button("Delete record")
    if btn:
        b = DonarCRUD()
        status = b.delete(id)
        if status:
            st.success("Record Deleted Successfully")
        else:
            st.error("Record not Found")

# UPDATE
with tab5:
    # st.title("UPDATE")
    st.header("UPDATE BOOK RECORD")
    id = st.number_input("Enter Donar ID for Update:")
    name = st.text_input("Enter Donar Name for Update:")
    bloodgroup = st.text_input("Enter Blood Group for Update:")
    phone = st.text_input("Phone for Update:")
    city = st.text_input("City for Update::")
    last_donation = st.date_input("Last Donation for Update:")
    btn = st.button("Update Donar")
    if btn:
        b = DonarCRUD()
        status = b.put(name, bloodgroup, phone, city, last_donation, id)
        if status:
            st.success("Update Successfully")
        else:
            st.error("No Record Found")

