import streamlit as st
import pickle as pkl
import numpy as np
from scipy.special import rel_entr
import time


def load_data():
    with open('heart_pred.pkl','rb') as file:
        data = pkl.load(file)
    return data

data = load_data()

df = data['dataframe']
model = data['model']


def check_datadrift(P,Q):
    return sum((rel_entr(P,Q)))

def predicted_page():
    
    st.image('14-512.webp',width=200)
    st.title('HEARTC')
    st.write("")
    cols = st.columns([1,10,1])
    cols[1].write("""### Enter the above test result and click on check""")
    st.write("")
    
    f_list=[]
    
    age = cols[1].slider('Age',min_value=15,max_value=100,value=30)
    f_list.append(age)
    
    cpt = cols[1].slider('Chest Pain Type',min_value=0,max_value=4,value=1)
    f_list.append(cpt) 
    
    bp = cols[1].number_input('BP')
    f_list.append(bp)
    
    chol = cols[1].number_input('Cholesterol')
    f_list.append(chol)
    
    fbs_over = cols[1].slider('FBS over 120', min_value=0, max_value=1, value=0)
    f_list.append(fbs_over)
    
    ekg_res = cols[1].slider('EKG result',min_value=0, max_value=2, value=1)
    f_list.append(ekg_res)
    
    max_hr = cols[1].number_input('Max HR')
    f_list.append(max_hr)
    
    ex_ang = cols[1].slider('Exercise angina',min_value=0,max_value=1,value=0)
    f_list.append(ex_ang)
    
    st_dep = cols[1].number_input('ST depression')
    f_list.append(st_dep)
    
    slp_of_st = cols[1].slider('Slope of ST', min_value=1, max_value=3, value=1)
    f_list.append(slp_of_st)
    
    no_of_vessel_fluro = cols[1].slider('Number of vessel Fluro',min_value=0, max_value=3, value=1 )
    f_list.append(no_of_vessel_fluro)
    
    thallium = cols[1].slider('Thallium', min_value=3,max_value=7,value=4)
    f_list.append(thallium)
    st.write("")
    cols = st.columns([2,1,2])
    
    check = cols[1].button("Check")

    stan = []
    base = []
    
    stan.append(df['Age'].mean())
    stan.append(df['BP'].mean())
    stan.append(df['Cholesterol'].mean())
    stan.append(df['ST depression'].mean())
    
    base.append(age)
    base.append(bp)
    base.append(chol)
    base.append(st_dep)
    
    if check:
        if len(f_list)<4:
            st.warning(""" ###Fill out all the values """)
        else:
            with st.spinner('Processing...'):
                time.sleep(5)
            
            
            val = check_datadrift(stan,base)
            if val >= 0.000:
                f_list = np.array(f_list)
                f_list = f_list.reshape(1,-1)
                flag = data['model'].predict(f_list)
                if flag == 1:
                    st.success('Present')
                else:
                    st.error('Absent')
            else:
                st.warning('Values are changed from the expected range.')
            
