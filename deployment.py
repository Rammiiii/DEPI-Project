import streamlit as st

def convert_categorical_to_numarical(value,category):
    if category== 'gender':
        if value == 'Male':
            return 1
        else:
            return 0
    elif category== 'ever_married':
        if value == 'Yes':
            return 1
        else:
            return 0
    elif category== 'work_type':
        if value == 'Govt_job':
            return 0
        elif value == 'Never_worked':
            return 1
        elif value == 'Private':
            return 2
        elif value == 'Self-employed':
            return 3
        else:
            return 4
    elif category== 'residence_type':
        if value == 'Urban':
            return 0
        else:
            return 1
    elif category== 'smoking_status':
        if value == 'Passive Smoker':
            return 0
        elif value == 'formerly smoked':
            return 1
        elif value == 'never smoked':
            return 2
        else:
            return 3



model_path =r'D:\data science\project_depi\DEPI-Project\stroke_prediction_model.pkl'
st.title("Stroke Prediction Application")
st.write("Enter the following details to predict the likelihood of a stroke:")
age = st.number_input("Age", min_value=0, max_value=120, value=30)
hypertension = st.selectbox("Hypertension (0 = No, 1 = Yes)", options=[0, 1])
heart_disease = st.selectbox("Heart Disease (0 = No, 1 = Yes)", options=[0, 1])
avg_glucose_level = st.number_input("Average Glucose Level", min_value=0.0, value=100.0)
bmi = st.number_input("BMI", min_value=0.0, value=25.0)
gender = convert_categorical_to_numarical( st.selectbox("Gender", options=["Male", "Female", "Other"]),'gender')
ever_married = convert_categorical_to_numarical( st.selectbox("Ever Married", options=["Yes", "No"]),'ever_married')

work_type = convert_categorical_to_numarical( st.selectbox("Work Type", options=["Private", "Self-employed", "Govt_job", "children", "Never_worked"]),'work_type')
Residence_type = convert_categorical_to_numarical( st.selectbox("Residence Type", options=["Urban", "Rural"]),'residence_type')
smoking_status = convert_categorical_to_numarical( st.selectbox("Smoking Status", options=["never smoked", "formerly smoked", "smokes", "unknown"]),'smoking_status')



if st.button("Predict Stroke"):

    import pandas as pd
    import pickle

    # Load the model
    with open(model_path, 'rb') as file:
        model = pickle.load(file)

    # Prepare the input data
    input_data = pd.DataFrame({
        'gender': [gender],
        'age': [age],
        'hypertension': [hypertension],
        'heart_disease': [heart_disease],
        'ever_married': [ever_married],
        'work_type': [work_type],
        'Residence_type': [Residence_type],
        'avg_glucose_level': [avg_glucose_level],
        'bmi': [bmi],
        'smoking_status': [smoking_status],
    })


    # Make the prediction
    prediction = model.predict(input_data)

    # Display the result
    if prediction[0] == 1:
        st.success("The model predicts a high likelihood of stroke.")
    else:
        st.success("The model predicts a low likelihood of stroke.")
