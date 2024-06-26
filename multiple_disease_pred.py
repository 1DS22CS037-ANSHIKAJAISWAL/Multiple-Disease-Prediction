# -*- coding: utf-8 -*-
"""
Created on Sat May  4 21:02:29 2024

@author: EG
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved models

diabetes_model=pickle.load(open('C:/Users/EG/Documents/Multiple Disease Prediction System/diabetes_model.sav','rb'))

heart_desease_model=pickle.load(open('C:/Users/EG/Documents/Multiple Disease Prediction System/heart_disease_model.sav','rb'))

parkinsons_model=pickle.load(open('C:/Users/EG/Documents/Multiple Disease Prediction System/parkinsons_model.sav','rb'))


# sidebar for navigate

with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           icons=['activity','heart','person'],
                           default_index=0)

# Diabetes Prediction Page
if (selected=='Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    #getting the input data from the user
    #columns for input fields
    col1,col2,col3=st.columns(3)
    
    with col1:
        Pregnancies=st.text_input("Number of Pregnancies")
    with col2:
        Glucose=st.text_input("Glucose Level")
    with col3:
        BloodPressure=st.text_input("Blood Pressure Value")
    with col1:
        SkinThickness=st.text_input("Skin Thickness Value")
    with col2:
        Insulin=st.text_input("Insulin Level")
    with col3:
        BMI=st.text_input("BMI Value")
    with col1:
        DiabetesPedigreeFunction=st.text_input("Diabetes Pedigree Function Value")
    with col2:
        Age=st.text_input("Age of the person")
        
        
        
        
        
    
   
    
   
    
    
   
   
   
    
    # code for Prediction
    diab_diagnosis=''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction=diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin, BMI,DiabetesPedigreeFunction,Age]])
    
        if (diab_prediction[0]==1):
            diab_diagnosis='The Person is Diabetic'
        else:
            diab_diagnosis='The person is not Diabetic'
            
    st.success(diab_diagnosis)
    
    
if (selected=='Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    #getting the input data from the user
    #columns for input fields
    col1,col2,col3=st.columns(3)
    
    with col1:
        age=st.text_input("Age")
    with col2:
        sex=st.text_input("Sex")
    with col3:
        cp=st.text_input("Chest Pain types")
    with col1:
        trestbps=st.text_input("Resting Blood Pressure")
    with col2:
        chol=st.text_input("Serum Cholestoral in mg/dL")
    with col3:
        fbs=st.text_input("Fasting Blood Sugar > 120 mg/dL")
    with col1:
        restecg=st.text_input("Resting Electrocardiographic results")
    with col2:
        thalach=st.text_input("Maximum  Heart Rate achieved")
    with col3:
        exang=st.text_input("Exercise Induced Angina")
    with col1:
        oldpeak=st.text_input("ST depression induced by exercise")
    with col2:
        slope=st.text_input("Slope of the peak exercise ST segment")
    with col3:
        ca=st.text_input("Major vessels colored by flourosopy")
    with col1:
        thal=st.text_input("thal: 0 =normal; 1=fixed defect; 2= reversable defect")
        
        
        
        
        
    
   
    
   
    
    
   
   
   
    
    # code for Prediction
    heart_predict=''
    
    # creating a button for Prediction
    
    if st.button('Heart Test Result'):
        heart_prediction=diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin, BMI,DiabetesPedigreeFunction,Age]])
    
        if (heart_prediction[0]==1):
            heart_diagnosis='The Person is Diabetic'
        else:
            heart_diagnosis='The person is not Diabetic'
            
    st.success(heart_predict)
    
    
if (selected=='Parkinsons Prediction'):
    
    # page title
    st.title('Parkinsons Prediction using ML')
    
    #getting the input data from the user
    #columns for input fields
    col1,col2,col3,col4,col5=st.columns(5)
    
    with col1:
        fo=st.text_input("MDVP:Fo(Hz)")
    with col2:
        fhi=st.text_input("MDVP:Fhi(Hz)")
    with col3:
        fio=st.text_input("MDVP:Flo(Hz)")
    with col4:
        Jitter_percent=st.text_input("MDVP:Jitter(%)")
    with col5:
        Jitter_Abs=st.text_input("MDVP:Jitter(Abs)")
    with col1:
        RAP=st.text_input("MDVP:RAP")
    with col2:
        PPQ=st.text_input("MDVP:PPQ")
    with col3:
        Jitter=st.text_input("Jitter:DDP")
    with col4:
        shimmer=st.text_input("MDVP:Shimmer")
    with col5:
        shimmer_db=st.text_input("MDVP:Shimmer(dB)")
    with col1:
        shimmer_apq3=st.text_input("Shimmer:APQ3")
    with col2:
        shimmer_apq5=st.text_input("Shimmer:APQ5")
    with col3:
        MDVP_APQ=st.text_input("MDVP:APQ")
    with col4:
        shimmer_dda=st.text_input("Shimmer:DDA")
    with col5:
        nhr=st.text_input("NHR")
    with col1:
        hnr=st.text_input("HNR")
    with col2:
        rdpe=st.text_input("RPDE")
    with col3:
        dfa=st.text_input("DFA")
    with col4:
        spread1=st.text_input("spread1")
    with col5:
        spread2=st.text_input("spread2")
    with col1:
        d2=st.text_input("D2")
    with col2:
        ppe=st.text_input("PPE")
        
        
        
        
        
    
   
    
   
    
    
   
   
   
    
    # code for Prediction
    perk_diagnosis=''
    
    # creating a button for Prediction
    
    if st.button('Perkinsons Test Result'):
        perk_prediction=diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin, BMI,DiabetesPedigreeFunction,Age]])
    
        if (perk_prediction[0]==1):
            perk_diagnosis='The Person is Diabetic'
        else:
            perk_diagnosis='The person is not Diabetic'
            
    st.success(perk_diagnosis)
    
