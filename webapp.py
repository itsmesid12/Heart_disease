import streamlit as st
import pickle as pkl
import pandas as pd

def load_data():
    with open('heart_pred.pkl','rb') as file:
        data = pkl.load(file)
    return data

data = load_data()

df = data['dataframe']
model = data['model']


def predicted_page():
    
    st.title('HEARTC')
    st.write("")
    cols = st.columns([1,8,1])
    cols[1].write("""### Enter the above test result and click on check""")
    st.write("")
    
    f_list=[]
    
    age = cols[1].slider('Age',min_value=15,max_value=100,value=30)
    f_list.append(age)
    
    check = cols[1].button("Check")

predicted_page()
