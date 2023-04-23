import streamlit as st
import helper
import pickle


model = pickle.load(open('rf.pkl','rb'))

st.header('Identify whether the below-given questions are semantically the same or not')

q1 = st.text_input('Enter question 1')
q2 = st.text_input('Enter question 2')

if st.button('Find'):
    query = helper.query_point_creator(q1,q2)
    result = model.predict(query)[0]

    if result:
        st.header('The above questions are duplicate')
    else:
        st.header('The above questions are different')


