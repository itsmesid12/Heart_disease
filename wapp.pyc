import streamlit as st
from predict_page import predicted_page
from Docs import docs
from mmdoc import model_monitoring_doc

c1,c2 = st.sidebar.columns([4,3])
c1.image('14-512.webp',width=150)
c2.write('')
c2.write('')
c2.write('')
c2.write('### HeartC ')

st.sidebar.write('')
st.sidebar.write('')

opt = st.sidebar.selectbox('Menu',['Documentation','HeartC','EDA','Model Monitoring'])

if opt == 'Documentation':
    docs()
elif opt == 'HeartC':
    predicted_page()
elif opt == 'EDA':
    st.write('Exploritary Data Analysis')
else:
    model_monitoring_doc()