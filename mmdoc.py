import streamlit as st


def model_monitoring_doc():
    
    st.image('14-512.webp',width=200)
    head = st.container()
    body = st.container()
    
    with head:
        st.title('Model Monitoring Docs')
        
        st.write('Why Machine Learning models in producion needs to be monitored?')
        
    with body:
        st.title('Production Challenges')
        
        st.markdown('* **Data distribution changes** - Why are there sudden changes in the values of my features?')
        st.markdown('* **Training-Serving Skew** - Why model is generating poor results in production despite our rigorous testing and validation attempts during development?')
        st.markdown('* **Model/Concept drift** - Why a well performing model in production suddenly dipped over time?')
        st.markdown('* **Black Box models** - How to interpret and explain model\'s predictions in line with the business objective and to relevant stakeholders?')
        st.markdown('* **Model Readiness** - How to compare results from a newer version(s) of my model against the in-production version(s)')
        st.markdown('* **Pipeline health issues** - why does the pipeline fail when executed/ why retraining job takes so long to run?')
        st.markdown('* **Cases of extreme events(Outliers)** - How to track the effect and performace of the model in extreme and unplanned situations?')
        st.markdown('* **Data Quality Issues** - How to ensure the production data is being processed in the same way as the training data?')
        