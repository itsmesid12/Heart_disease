import streamlit as st
import pandas as pd

def docs():
    
    st.image('14-512.webp',width=200)
    head = st.container()
    dataset = st.container()
    features = st.container()
    model_training = st.container()

    with head:
        st.title('Welcome to HEARTC Demo')
        st.header('For this demo I\'ve taken Heart disease prediction')
    
    with dataset:
        st.header('Heart Disease Prediction')
        st.text('The dataset was taken from Kaggle.')
    
        heart_data = pd.read_csv('Dataset/Heart_Disease_Prediction.csv')
        st.write(heart_data.head())
    
    with features:
        st.header('The Features List')
    
        st.markdown('* **Age** -  The most important risk factor in developing cardiovascular or heart diseases, with approximately a tripling of risk with each decade of life. The risk of stroke doubles every decade after age 55')
        st.markdown('* **Gender** - Men are at greater risk of heart disease than pre-menopausal women.If a female has diabetes, she is more likely to develop heart disease than a male with diabetes.')
        st.markdown('* **Chest pain type** \n1: Typical angina\n2: Atypical angina3\n3:Non-anginal pain\n4: Asymptomatic')
        st.markdown('* **Blood pressure** -  High blood pressure can damage arteries that feed your heart. High blood pressure that occurs with other conditions, such as obesity, high cholesterol or diabetes, increases your risk even more.')
        st.markdown('* **Cholesterol** - A high level of low-density lipoprotein (LDL) cholesterol (the “bad” cholesterol) is most likely to narrow arteries.')
        st.markdown('* **FBS over 120** - Not producing enough of a hormone secreted by pancreas (insulin) or not responding to insulin properly causes your body’s blood sugar levels to rise, increasing your risk of a heart attack.')
        st.markdown('* **EKG/ECG results** - Displays resting electrocardiographic results\n0 = normal\n1 = having ST-T wave abnormality\n2 = left ventricular hyperthrophy ')
        st.markdown('* **Max HR** - The increase in cardiovascular risk, associated with the acceleration of heart rate, was comparable to the increase in risk observed with high blood pressure. ')
        st.markdown('* **Exercise angina** - Angina (Chest Pain): Angina is chest pain or discomfort caused when heart muscle doesn’t get enough oxygen-rich blood. The discomfort also can occur in your shoulders, arms, neck, jaw, or back. Angina pain may even feel like indigestion.')
        st.markdown('* **ST depression** - Exercise ECGs with up-sloping ST-segment depressions are typically reported as an ‘equivocal’ test. The duration of ST-segment depression is also important, as prolonged recovery after peak stress is consistent with a positive treadmill ECG stress test.')
        st.markdown('* **Slope of ST** - The occurrence of horizontal or down-sloping ST-segment depression at a lower workload (calculated in METs) or heart rate indicates a worse prognosis and higher likelihood of multi-vessel disease.')
        st.markdown('* **Thallium** - Displays the thalassemia :')
        st.markdown('** 3 = normal')
        st.write('** 6 = fixed defect')
        st.write('     7 = reversible defect')
        
        with model_training:
            st.header('Model training Phase')