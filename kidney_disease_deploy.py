import streamlit as st
import pandas as pd
import pickle as pk

model = pk.load(open("classifier_kidney.pkl","rb"))
scaler = pk.load(open("scaler_kidney.pkl","rb"))

title = st.title("Kidney Disease Prediction 🩺")

age = st.slider("What is your Age?", 2, 100)
bp = st.slider('Select Blood Pressure (mmHg)', min_value = 50, max_value = 200, value = 80)   # mmHg : millimeters of mercury — it's the unit of measurement for blood pressure
sg = st.slider('Select Specific Gravity (SG)', min_value = 1.000, max_value = 1.030, value = 1.020, step = 0.001)
al = st.slider('Select Albumin', 0.0, 5.0)
su = st.slider('Select Sugar', 0.0, 5.0)
rbc = st.radio("Choose Red Blood Cells Level (rbc)",["normal","abnormal"])
pc = st.radio("Choose Pus Cells Level",['normal','abnormal'])
pcc = st.radio("Pus Cells Clumps",['present','notpresent'])
ba = st.radio("Bacteria",['present','notpresent'])
bgr = st.slider("Select Blood Glucose Random", 50, 500)
bu = st.slider("Select Blood Urea", 0, 300)
sc = st.slider("Select Serum Creatinine", 0.05, 50.0)
sod = st.slider("Select Sodium Level", 4, 150)
pot = st.slider("Select Potassium Level", 4,150)
hemo = st.slider("Select Haemoglobin", 4.0, 20.0, 5.0, 0.1)
pcv = st.slider("Packed Cell Volume", 8, 55, 44, step=1)
wc = st.slider("White Blood Cell Count", 2000, 20000, 7800, step=100)
rc = st.slider("Red Blood Cell Count", 2.0, 8.0, 5.2, step=0.1)
htn = st.radio("Hypertension", ["yes", "no"])
dm = st.radio("Diabetes Mellitus", ["yes", "no"])
cad = st.radio("Coronary Artery Disease", ["yes","no"])
appet = st.radio("Appetite", ["good", "poor"])
pe = st.radio("Pedal Edema", ["yes","no"])
ane = st.radio("Anemia", ["yes","no"])

rbc = 1 if rbc == "normal" else 0
pc = 1 if pc == "normal" else 0
pcc = 1 if pcc == "present" else 0
ba = 1 if ba == "present" else 0
htn = 1 if htn == "yes" else 0
dm = 1 if dm == "yes" else 0
cad = 1 if cad == "yes" else 0
appet = 1 if appet == "good" else 0
pe = 1 if pe == "yes" else 0
ane = 1 if ane == "yes" else 0

if st.button("Predict"):
    pred_data = pd.DataFrame([[age, bp, sg, al, su, rbc, pc, pcc, ba, bgr, bu,
                                sc, sod, pot, hemo, pcv, wc, rc, htn, dm, cad,
                                appet, pe, ane ]],
                                columns = ['age', 'bp', 'sg', 'al', 'su', 'rbc', 'pc', 'pcc', 'ba', 'bgr', 'bu',
                                            'sc', 'sod', 'pot', 'hemo', 'pcv', 'wc', 'rc', 'htn', 'dm', 'cad',
                                            'appet', 'pe', 'ane'])
    
    scaled_data = scaler.transform(pred_data)
    prediction = model.predict(scaled_data)
    if prediction[0] == 1:
        st.error("You may have Chronic Kidney Disease. Please consult a doctor.")
    else:
        st.success("You do not have Chronic Kidney Disease.")