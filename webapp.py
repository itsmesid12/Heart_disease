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
    cols = st.columns([1,10,1])
    cols[1].write("""### Enter the above test result and click on check""")
    st.write("")
    
    f_list=[]
    
    age = cols[1].slider('Age',min_value=15,max_value=100,value=30)
    f_list.append(age)
    
    cpt = cols[1].number_input('Chest Pain Type')
    f_list.append(cpt) 
    
    bp = cols[1].number_input('BP')
    f_list.append(bp)
    
    chol = cols[1].number_input('Cholesterol')
    f_list.append(chol)
    
    fbs_over = cols[1].number_input('FBS over')
    f_list.append(fbs_over)
    
    ekg_res = cols[1].number_input('EKG result')
    f_list.append(ekg_res)
    
    max_hr = cols[1].number_input('Max HR')
    f_list.append(max_hr)
    
    ex_ang = cols[1].number_input('Exercise angina')
    f_list.append(ex_ang)
    
    st_dep = cols[1].number_input('ST depression')
    f_list.append(st_dep)
    
    slp_of_st = cols[1].number_input('Slope of ST')
    f_list.append(slp_of_st)
    
    no_of_vessel_fluro = cols[1].number_input('Number of vessel Fluro')
    f_list.append(no_of_vessel_fluro)
    
    thallium = cols[1].number_input('Thallium')
    f_list.append(thallium)
    st.write("")
    cols = st.columns([2,1,2])
    
    check = cols[1].button("Check")
    
    if check:
        if len(f_list)<2:
            st.warning("""###Fill out all the values """)
                
predicted_page()
